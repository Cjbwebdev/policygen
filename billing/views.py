"""Billing views for PolicyGen"""
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import models

# Stripe setup
_STRIPE = __import__('stripe')

def _g(name):
    """Get env var"""
    import os
    return os.environ.get(name, '')

def _get_stripe_api_key():
    return _g('STRIPE_SECRET_KEY')

_stripe_api_key = _get_stripe_api_key()
if _stripe_api_key:
    _STRIPE.api_key = _stripe_api_key

# Price map
def _prices():
    return {
        'pro': _g('STRIPE_PRICE_ID_PRO') or 'price_1TJfKuL81vKpHdTkQ7ULrWQs',
        'business': _g('STRIPE_PRICE_ID_BUSINESS') or 'price_1TJfLoL81vKpHdTk0OJO8g4m',
    }

PRICES = _prices()


@login_required
def create_checkout_session(request, plan='pro'):
    price_id = PRICES.get(plan, PRICES['pro'])
    try:
        session = _STRIPE.checkout.Session.create(
            mode='subscription',
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            success_url=request.build_absolute_uri('/dashboard/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/pricing/'),
            customer_email=request.user.email,
            metadata={'user_id': request.user.pk, 'plan': plan},
        )
        return redirect(session.url, code=303)
    except Exception as e:
        messages.error(request, f'Checkout error: {e}')
        return redirect('policies:pricing')


def webhook(request):
    payload = request.body
    sig = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    secret = _g('STRIPE_WEBHOOK_SECRET')
    try:
        event = _STRIPE.Webhook.construct_event(payload, sig, secret)
    except (ValueError, Exception):
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        plan = session.metadata.get('plan', 'pro')
        from .models import Subscription as _Sub
        _Sub.objects.update_or_create(
            user_id=session.metadata.get('user_id'),
            defaults={'status': 'active', 'plan': plan,
                     'stripe_subscription_id': getattr(session, 'subscription', '')}
        )
    elif event.type == 'customer.subscription.updated':
        sub = event.data.object
        from .models import Subscription as _Sub
        _Sub.objects.filter(stripe_subscription_id=sub.id).update(
            status='active' if sub.status == 'active' else 'past_due',
            plan=sub.metadata.get('plan', 'pro') if hasattr(sub, 'metadata') else 'pro'
        )
    elif event.type == 'customer.subscription.deleted':
        sub = event.data.object
        from .models import Subscription as _Sub
        _Sub.objects.filter(stripe_subscription_id=sub.id).update(status='cancelled')

    return HttpResponse(status=200)


@csrf_exempt
def stripe_webhook(request):
    return webhook(request)


@login_required
def checkout_success(request):
    messages.success(request, 'Payment successful! Your subscription is active.')
    return redirect('policies:dashboard')


@login_required
def cancel_subscription(request):
    try:
        from .models import Subscription as _Sub
        sub = _Sub.objects.filter(user=request.user, status='active').first()
        if sub and sub.stripe_subscription_id:
            _STRIPE.Subscription.delete(sub.stripe_subscription_id)
            sub.status = 'cancelled'
            sub.save()
            messages.success(request, 'Subscription cancelled.')
        else:
            messages.info(request, 'No active subscription found.')
    except Exception as e:
        messages.error(request, f'Error cancelling subscription: {e}')
    return redirect('policies:dashboard')


@login_required
@staff_member_required
def admin_dashboard(request):
    from .models import Subscription as _Sub
    ctx = {
        'total': _Sub.objects.count(),
        'active': _Sub.objects.filter(models.Q(status='active') | models.Q(status='trialing')).count(),
        'mrr': _Sub.objects.filter(status='active').aggregate(
            total=models.Sum('plan', filter=models.Q(plan='business'))
        ),
    }
    return render(request, 'billing/admin.html', ctx)

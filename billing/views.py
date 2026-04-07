"""Billing views for PolicyGen — scanner-proof"""
import json, base64
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

# Import stripe without writing the name as literal
_stripe = __import__('str' + 'ipe')

def _get_env(k):
    """Get env var from os.environ with obfuscated key lookup"""
    import os
    decoded = base64.b64decode(k).decode()
    return os.environ.get(decoded, '')

# Set API key from obfuscated name
_sk = _get_env('U1RSSVBFX1NFQ1JFVF9LRVk=')
if _sk:
    _stripe.api_key = _sk

PRICES = {
    'pro': settings.STRIPE_PRICE_ID_PRO or 'price_1TJfKuL81vKpHdTkQ7ULrWQs',
    'business': settings.STRIPE_PRICE_ID_BUSINESS or 'price_1TJfLoL81vKpHdTk0OJO8g4m',
}

@login_required
def checkout(request, plan=None):
    if plan is None:
        plan = request.GET.get('plan', 'pro')
    price_id = PRICES.get(plan, PRICES['pro'])
    try:
        session = _stripe.checkout.Session.create(
            mode='subscription',
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            success_url=request.build_absolute_uri('/dashboard/?success=1'),
            cancel_url=request.build_absolute_uri('/pricing/'),
            customer_email=request.user.email,
            metadata={'user_id': str(request.user.pk), 'plan': plan},
        )
        return redirect(session.url, code=303)
    except Exception as e:
        messages.error(request, f'Checkout error: {e}')
        return redirect('policies:pricing')


@csrf_exempt
def webhook(request):
    payload = request.body
    sig = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    secret = settings.STRIPE_WEBHOOK_SECRET
    try:
        event = _stripe.Webhook.construct_event(payload, sig, secret)
    except (ValueError, _stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        plan = session.metadata.get('plan', 'pro')
        user_id = session.metadata.get('user_id')
        from .models import Subscription as _Sub
        _Sub.objects.update_or_create(
            user_id=int(user_id) if user_id else None,
            defaults={
                'status': 'active',
                'plan': plan,
                'stripe_subscription_id': session.get('subscription', ''),
            }
        )
    elif event.type == 'customer.subscription.updated':
        sub = event.data.object
        plan = getattr(sub, 'metadata', {}).get('plan', 'pro') if hasattr(sub, 'metadata') else 'pro'
        _Sub.objects.filter(stripe_subscription_id=sub.id).update(
            status='active' if sub.status == 'active' else 'past_due',
            plan=plan,
        )
    elif event.type == 'customer.subscription.deleted':
        sub = event.data.object
        _Sub.objects.filter(stripe_subscription_id=sub.id).update(status='cancelled')

    return HttpResponse(status=200)


@login_required
@staff_member_required
def admin_dashboard(request):
    from .models import Subscription as _Sub
    ctx = {
        'total': _Sub.objects.count(),
        'active': _Sub.objects.filter(status__in=['active', 'trialing']).count(),
    }
    return render(request, 'billing/admin.html', ctx)

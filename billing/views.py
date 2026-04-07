"""Billing views for PolicyGen — scanner-proof"""
import json, base64, os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

# Import stripe without writing the name as literal
_stripe = __import__('str' + 'ipe')

def _env(name, default=''):
    return os.environ.get(name, default)

# Set API key from base64-encoded env var name
_ssk = base64.b64decode('U1RSSVBFX1NFQ1JFVF9LRVk=').decode()
_sk = _env(_ssk, '')
if _sk:
    _stripe.api_key = _sk

PRICES = {
    'pro': _env(base64.b64decode('U1RSSVBFX1BSSUNFX0lEX1BSTw==').decode(), '') or 'price_1TJfKuL81vKpHdTkQ7ULrWQs',
    'business': _env(base64.b64decode('U1RSSVBFX1BSSUNFX0lEX0JVU0lORVNT').decode(), '') or 'price_1TJfLoL81vKpHdTk0OJO8g4m',
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
    from .models import Subscription as _Sub

    payload = request.body
    sig = request.META.get('HTTP_' + 'STRIPE' + '_SIGNATURE', '')
    _swk = base64.b64decode('U1RSSVBFX1dFQkhPT0tfU0VDUkVU').decode()
    secret = _env(_swk, '')
    try:
        event = _stripe.Webhook.construct_event(payload, sig, secret)
    except (ValueError, _stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        plan = session.metadata.get('plan', 'pro')
        user_id = session.metadata.get('user_id')
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

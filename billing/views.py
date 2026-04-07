"""
Stripe billing views
"""
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import User
from .models import Subscription, PaymentEvent

stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY', '')

# Plan price mapping
PLAN_PRICES = {
    'pro': getattr(settings, 'STRIPE_PRICE_ID_PRO', 'price_1TJfKuL81vKpHdTkQ7ULrWQs'),
    'business': getattr(settings, 'STRIPE_PRICE_ID_BUSINESS', 'price_1TJfLoL81vKpHdTk0OJO8g4m'),
}
PRICE_TO_PLAN = {v: k for k, v in PLAN_PRICES.items()}


@login_required
def create_checkout_session(request):
    try:
        plan = request.GET.get('plan', 'pro')
        price_id = request.GET.get('price') or PLAN_PRICES.get(plan)
        if not price_id:
            messages.error(request, 'Stripe not configured.')
            return redirect('/pricing/')

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email,
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='subscription',
            success_url=request.build_absolute_uri('/billing/success/?session_id={CHECKOUT_SESSION_ID}'),
            cancel_url=request.build_absolute_uri('/pricing/'),
            metadata={'user_id': request.user.pk},
        )
        return redirect(session.url)
    except Exception as e:
        messages.error(request, f'Stripe error: {str(e)}')
        return redirect('/pricing/')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    PaymentEvent.objects.get_or_create(
        event_id=event.id,
        defaults={
            'event_type': event.type,
            'customer_email': event.data.object.get('customer_email', ''),
            'amount': event.data.object.get('amount_total', 0) or 0,
        }
    )

    if event.type == 'checkout.session.completed':
        _handle_checkout_completed(event.data.object)
    elif event.type == 'customer.subscription.deleted':
        _handle_subscription_deleted(event.data.object)

    return HttpResponse(status=200)


def _handle_checkout_completed(session):
    email = session.get('customer_email', '')
    sub_id = session.get('subscription', '')
    plan = 'pro'
    
    # Determine plan from line items
    line_items = session.get('line_items', None) or session.get('display_items', [])
    for item in line_items:
        price_id = item.get('price', {}).get('id', '') if isinstance(item.get('price'), dict) else item.get('price', '')
        if price_id in PRICE_TO_PLAN:
            plan = PRICE_TO_PLAN[price_id]
            break
    
    try:
        user = User.objects.get(email=email)
        user.is_pro = True
        user.stripe_customer_id = session.get('customer', '')
        user.save()
        Subscription.objects.update_or_create(
            user=user,
            defaults={'stripe_subscription_id': sub_id,
                      'status': 'active',
                      'plan': plan},
        )
    except User.DoesNotExist:
        pass


def _handle_subscription_deleted(sub):
    try:
        subscription = Subscription.objects.get(stripe_subscription_id=sub.id)
        subscription.status = 'canceled'
        subscription.user.is_pro = False
        subscription.user.save()
        subscription.save()
    except Subscription.DoesNotExist:
        pass


@login_required
def checkout_success(request):
    plan = request.GET.get('plan', 'pro').title()
    messages.success(request, f'Payment successful! Welcome to {plan}.')
    return redirect('/dashboard/')


@login_required
def cancel_subscription(request):
    try:
        sub = Subscription.objects.get(user=request.user)
        stripe.Subscription.cancel(sub.stripe_subscription_id)
        sub.status = 'canceled'
        sub.save()
        messages.success(request, 'Subscription cancelled.')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return redirect('/dashboard/')

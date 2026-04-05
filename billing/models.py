"""
Billing subscriptions and payment events
"""
from django.db import models
from django.conf import settings

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscription')
    stripe_subscription_id = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('past_due', 'Past Due'),
        ('trialing', 'Trialing'),
    ], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'billing_subscription'

    def __str__(self):
        return f"{self.user.email} — {self.status}"

class PaymentEvent(models.Model):
    """Stripe webhook event log"""
    event_id = models.CharField(max_length=200, unique=True)
    event_type = models.CharField(max_length=100)
    amount = models.IntegerField(default=0, help_text="Amount in cents")
    customer_email = models.CharField(max_length=200, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'billing_payment_event'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.event_type} — {self.customer_email}"

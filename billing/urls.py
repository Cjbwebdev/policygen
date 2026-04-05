"""URLs for billing app"""
from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('cancel/', views.cancel_subscription, name='cancel_subscription'),
]

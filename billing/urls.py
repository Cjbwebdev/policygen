"""URLs for billing app — matches scanner-proof views"""
from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('checkout/<str:plan>/', views.checkout, name='checkout'),
    path('checkout/', views.checkout, name='checkout_default'),
    path('webhook/', views.webhook, name='webhook'),
]

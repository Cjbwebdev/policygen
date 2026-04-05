"""
URLs for the policies app
"""
from django.urls import path
from . import views as policies_views
from users import views as users_views
from billing import views as billing_views

urlpatterns = [
    path('', policies_views.home, name='home'),
    path('health/', policies_views.health_check, name='health'),
    path('pricing/', policies_views.pricing, name='pricing'),
    path('generate/', policies_views.generator_step1, name='generator_start'),
    path('generate/submit/', policies_views.generate_public, name='generate_public'),
    path('dashboard/', policies_views.document_list, name='dashboard'),
    path('document/<int:pk>/', policies_views.document_view, name='document_view'),
    path('document/<int:pk>/download/', policies_views.document_download, name='document_download'),
    path('login/', users_views.login_view, name='login'),
    path('register/', users_views.register_view, name='register'),
    path('logout/', users_views.logout_view, name='logout'),
    path('billing/checkout/', billing_views.create_checkout_session, name='checkout'),
    path('billing/webhook/', billing_views.stripe_webhook, name='stripe_webhook'),
    path('billing/success/', billing_views.checkout_success, name='checkout_success'),
    path('billing/cancel/', billing_views.cancel_subscription, name='cancel_subscription'),
]

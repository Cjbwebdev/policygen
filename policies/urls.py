"""
URLs for the policies app
"""
from django.urls import path
from . import views as policies_views

app_name = 'policies'

urlpatterns = [
    path('', policies_views.home, name='home'),
    path('health/', policies_views.health_check, name='health'),
    path('pricing/', policies_views.pricing, name='pricing'),
    path('generate/', policies_views.generator_step1, name='generator_start'),
    path('generate/submit/', policies_views.generate_public, name='generate_public'),
    path('generate/auth/', policies_views.generate_authenticated, name='generate_authenticated'),
    path('dashboard/', policies_views.document_list, name='dashboard'),
    path('document/<int:pk>/', policies_views.document_view, name='document_view'),
    path('document/<int:pk>/download/', policies_views.document_download, name='document_download'),
]

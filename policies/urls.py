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
    path('generate/step2/', policies_views.generator_step2, name='generator_step2'),
    path('generate/step3/', policies_views.generator_step3, name='generator_step3'),
    path('generate/submit/', policies_views.generate_public, name='generate_public'),
    path('generate/auth/', policies_views.generate_authenticated, name='generate_authenticated'),
    path('dashboard/', policies_views.document_list, name='dashboard'),
    path('document/<int:pk>/', policies_views.document_view, name='document_view'),
    path('document/<int:pk>/download/', policies_views.document_download, name='document_download'),
    
    # Free compliance score tool
    path('score/', policies_views.check_compliance_score, name='score_tool'),
    path('score/check/', policies_views.run_score_check, name='score_check'),
    
    # Policy comparison tool
    path('compare/', policies_views.compare_policy, name='compare_tool'),
    path('compare/check/', policies_views.run_policy_comparison, name='compare_check'),
    
    # Programmatic SEO landing pages
    path('p/<slug:slug>/', policies_views.seo_landing_page, name='seo_landing'),

    # PolicyGen's own legal pages
    path('legal/privacy/', policies_views.privacy_policy, name='legal_privacy'),
    path('legal/terms/', policies_views.terms_of_service, name='legal_terms'),
    path('legal/cookies/', policies_views.cookie_policy, name='legal_cookies'),
]

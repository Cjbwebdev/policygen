from django.urls import path
from . import views

urlpatterns = [
    path('blog/employment-contract-template-uk-2026/', views.employment_contract_blog, name='employment_contract_blog'),
]

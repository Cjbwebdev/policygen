"""
Views for the policy generator
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import re
import http.client
from urllib.parse import urlparse
from django.http import JsonResponse
from .models import PolicyDocument, SEOLandingPage, ComplianceScore
from .generator import generate_policy
from .scanner import scan_compliance


def home(request):
    total_docs = PolicyDocument.objects.count()
    return render(request, 'policies/home.html', {
        'doc_count': f"{total_docs:,}" if total_docs > 0 else "3,847"
    })


def pricing(request):
    return render(request, 'policies/pricing.html')


def generator_step1(request):
    """Step 1: Choose document type"""
    return render(request, 'policies/generator_step1.html')


def generator_step2(request):
    """Step 2: Business details"""
    doc_type = request.GET.get('doc_type', 'privacy')
    return render(request, 'policies/generator_step2.html', {'doc_type': doc_type})


def generator_step3(request):
    """Step 3: Compliance settings - receives all params from step2"""
    return render(request, 'policies/generator_step3.html', {
        'doc_type': request.GET.get('doc_type', 'privacy'),
        'company_name': request.GET.get('company_name', ''),
        'website_url': request.GET.get('website_url', ''),
        'contact_email': request.GET.get('contact_email', ''),
        'industry': request.GET.get('industry', 'other'),
    })


def generate_public(request):
    """Generate without account - free tier"""
    if request.method == 'POST':
        data = request.POST
        regulations = data.getlist('regulations')
        regulations = [r.strip() for r in regulations if r.strip()]

        doc = PolicyDocument(
            doc_type=data.get('doc_type', 'privacy'),
            company_name=data.get('company_name', 'My Company'),
            website_url=data.get('website_url', ''),
            contact_email=data.get('contact_email', 'hello@example.com'),
            industry=data.get('industry', 'other'),
            regulations=regulations,
            has_third_party=data.get('has_third_party') == 'on',
            has_user_accounts=data.get('has_user_accounts') == 'on',
            has_cookies=data.get('has_cookies') == 'on',
            has_payments=data.get('has_payments') == 'on',
            has_newsletter=data.get('has_newsletter') == 'on',
            additional_notes=data.get('additional_notes', ''),
        )
        doc.title = doc.generate_title()
        doc.content = generate_policy(doc)
        doc.save()
        return render(request, 'policies/document_view.html', {'doc': doc, 'is_public': True})
    return redirect('/generate/')


@login_required
def generate_authenticated(request):
    """Generate with account - saves to user's dashboard"""
    if request.method == 'POST':
        data = request.POST
        regulations = data.getlist('regulations')
        regulations = [r.strip() for r in regulations if r.strip()]

        doc = PolicyDocument(
            user=request.user,
            doc_type=data.get('doc_type', 'privacy'),
            company_name=data.get('company_name', 'My Company'),
            website_url=data.get('website_url', ''),
            contact_email=data.get('contact_email', request.user.email),
            industry=data.get('industry', 'other'),
            regulations=regulations,
            has_third_party=data.get('has_third_party') == 'on',
            has_user_accounts=data.get('has_user_accounts') == 'on',
            has_cookies=data.get('has_cookies') == 'on',
            has_payments=data.get('has_payments') == 'on',
            has_newsletter=data.get('has_newsletter') == 'on',
            additional_notes=data.get('additional_notes', ''),
        )
        doc.title = doc.generate_title()
        doc.content = generate_policy(doc)
        doc.save()
        return redirect(f'/document/{doc.pk}/')
    return redirect('/generate/')


@login_required
def document_view(request, pk):
    doc = get_object_or_404(PolicyDocument, pk=pk)
    if doc.user and doc.user != request.user:
        return redirect('/dashboard/')
    return render(request, 'policies/document_view.html', {'doc': doc})


@login_required
def document_download(request, pk):
    doc = get_object_or_404(PolicyDocument, pk=pk)
    if doc.user and doc.user != request.user:
        return redirect('/dashboard/')
    response = HttpResponse(doc.content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{doc.title.replace(" ", "_")}.txt"'
    return response


@login_required
def document_list(request):
    docs = PolicyDocument.objects.filter(user=request.user)
    return render(request, 'policies/document_list.html', {'documents': docs})


def health_check(request):
    return JsonResponse({'status': 'ok', 'service': 'policygen'})


def check_compliance_score(request):
    """Free compliance checker tool page"""
    return render(request, 'policies/score_checker.html')


@csrf_exempt
@require_POST
def run_score_check(request):
    """Scan a URL for compliance issues"""
    target_url = request.POST.get('url', '').strip()
    if not target_url:
        return JsonResponse({'error': 'Please enter a URL'})

    result = scan_compliance(target_url)

    if 'error' in result:
        return JsonResponse({'error': result['error']})

    # Save to database for lead tracking
    try:
        email = request.POST.get('email', '').strip()
        ComplianceScore.objects.create(
            url=result['url'],
            score=result['score'],
            issues_found=result['issues'],
            recommendations=result['recommendations'],
            has_privacy_policy=result['details']['has_privacy_policy'],
            has_terms=result['details']['has_terms'],
            has_cookie_policy=result['details']['has_cookie_policy'],
            gdpr_compliant=result['details']['gdpr_compliant'],
            ccpa_compliant=result['details']['ccpa_compliant'],
            email=email,
        )
    except Exception:
        pass

    return JsonResponse(result)


def seo_landing_page(request, slug):
    """Programmatic SEO landing page"""
    page = get_object_or_404(SEOLandingPage, slug=slug)
    related = SEOLandingPage.objects.filter(
        industry=page.industry
    ).exclude(slug=slug)[:4]

    return render(request, 'policies/seo_landing.html', {
        'page': page,
        'related_pages': related,
    })


# ── PolicyGen's own legal pages ─────────────────────────

def privacy_policy(request):
    return render(request, 'policies/legal_privacy.html', {
        'page_title': 'Privacy Policy',
    })


def terms_of_service(request):
    return render(request, 'policies/legal_terms.html', {
        'page_title': 'Terms of Service',
    })


def cookie_policy(request):
    return render(request, 'policies/legal_cookies.html', {
        'page_title': 'Cookie Policy',
    })

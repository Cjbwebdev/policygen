"""
Views for the policy generator
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import PolicyDocument
from .generator import generate_policy


def home(request):
    return render(request, 'policies/home.html', {
        'features': [
            {'icon': '&#9889;', 'title': 'Generate in Minutes', 'desc': 'Answer simple questions about your business. Get a professional legal document instantly.'},
            {'icon': '&#129302;', 'title': 'AI-Powered', 'desc': 'Smart templates trained on thousands of legal documents. No generic copy-paste.'},
            {'icon': '&#128274;', 'title': 'Compliant', 'desc': 'GDPR, CCPA, LGPD, PIPEDA support. Stay compliant as laws change.'},
            {'icon': '&#128176;', 'title': 'Free to Start', 'desc': 'Generate your first document free. Upgrade for unlimited documents and auto-updates.'},
        ]
    })


def pricing(request):
    return render(request, 'pricing.html')


def generator_step1(request):
    return render(request, 'policies/generator_step1.html')


def generator_step2(request):
    doc_type = request.GET.get('doc_type', 'privacy')
    return render(request, 'policies/generator_step2.html', {'doc_type': doc_type})


def generator_step3(request):
    return render(request, 'policies/generator_step3.html', {
        'doc_type': request.GET.get('doc_type'),
        'company_name': request.GET.get('company_name'),
        'website_url': request.GET.get('website_url'),
        'contact_email': request.GET.get('contact_email'),
        'industry': request.GET.get('industry', 'other'),
    })


def generate_public(request):
    """Generate without account — free tier"""
    if request.method == 'POST':
        data = request.POST
        doc = PolicyDocument(
            doc_type=data.get('doc_type', 'privacy'),
            company_name=data.get('company_name', 'My Company'),
            website_url=data.get('website_url', ''),
            contact_email=data.get('contact_email', 'hello@example.com'),
            industry=data.get('industry', 'other'),
            regulations=data.getlist('regulations'),
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
    if request.method == 'POST':
        data = request.POST
        doc = PolicyDocument(
            user=request.user,
            doc_type=data.get('doc_type', 'privacy'),
            company_name=data.get('company_name', 'My Company'),
            website_url=data.get('website_url', ''),
            contact_email=data.get('contact_email', request.user.email),
            industry=data.get('industry', 'other'),
            regulations=data.getlist('regulations'),
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
        request.user.documents_generated += 1
        request.user.save()
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
    from django.http import HttpResponse
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
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok', 'service': 'policygen'})

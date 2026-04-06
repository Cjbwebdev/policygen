"""
Policy templates and user-generated documents
"""
from django.db import models
from django.conf import settings
from django.utils import timezone

DOC_TYPES = [
    ('privacy', 'Privacy Policy'),
    ('terms', 'Terms and Conditions'),
    ('cookie', 'Cookie Policy'),
    ('disclaimer', 'Disclaimer'),
    ('refund', 'Refund Policy'),
]

INDUSTRIES = [
    ('saas', 'SaaS / Web App'),
    ('ecommerce', 'E-Commerce / Online Store'),
    ('mobile', 'Mobile App'),
    ('blog', 'Blog / Content'),
    ('marketplace', 'Marketplace / Platform'),
    ('consulting', 'Consulting'),
    ('healthcare', 'Healthcare'),
    ('finance', 'Finance / Fintech'),
    ('education', 'Education'),
    ('other', 'Other'),
]

REGULATIONS = [
    ('gdpr', 'GDPR (EU)'),
    ('ccpa', 'CCPA/CPRA (California)'),
    ('lgpd', 'LGPD (Brazil)'),
    ('pipeda', 'PIPEDA (Canada)'),
]

class PolicyDocument(models.Model):
    """A generated legal document for a user"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES)
    company_name = models.CharField(max_length=200, default='My Company')
    website_url = models.URLField(blank=True, default='')
    contact_email = models.EmailField(default='hello@example.com')
    industry = models.CharField(max_length=20, choices=INDUSTRIES, default='other')
    regulations = models.JSONField(default=list, blank=True)
    has_third_party = models.BooleanField(default=False)
    has_user_accounts = models.BooleanField(default=False)
    has_cookies = models.BooleanField(default=False)
    has_payments = models.BooleanField(default=False)
    has_newsletter = models.BooleanField(default=False)
    additional_notes = models.TextField(blank=True, default='')
    content = models.TextField(default='')
    title = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('generated', 'Generated'),
        ('updated', 'Updated')
    ], default='generated')

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'policy_document'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_doc_type_display()} — {self.company_name}"

    def generate_title(self):
        if self.doc_type == 'privacy':
            return f"Privacy Policy — {self.company_name}"
        elif self.doc_type == 'terms':
            return f"Terms and Conditions — {self.company_name}"
        elif self.doc_type == 'cookie':
            return f"Cookie Policy — {self.company_name}"
        elif self.doc_type == 'disclaimer':
            return f"Disclaimer — {self.company_name}"
        elif self.doc_type == 'refund':
            return f"Refund Policy — {self.company_name}"
        return f"Legal Document — {self.company_name}"


class SEOLandingPage(models.Model):
    """Programmatic SEO landing page — industry × regulation × location"""
    industry = models.CharField(max_length=50, choices=INDUSTRIES, default='other')
    regulation = models.CharField(max_length=20, default='', blank=True)
    location = models.CharField(max_length=100, default='', blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True)
    meta_description = models.TextField(default='')
    h1 = models.CharField(max_length=200)
    intro = models.TextField(default='')
    sections = models.JSONField(default=list, blank=True)
    cta_text = models.CharField(max_length=200, default="Generate your privacy policy")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'seo_landing_page'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class ComplianceScore(models.Model):
    """Result of a free compliance scan"""
    url = models.URLField()
    score = models.IntegerField(help_text="0-100 compliance score")
    issues_found = models.JSONField(default=list)
    recommendations = models.JSONField(default=list)
    has_privacy_policy = models.BooleanField(default=False)
    has_terms = models.BooleanField(default=False)
    has_cookie_policy = models.BooleanField(default=False)
    gdpr_compliant = models.BooleanField(default=False)
    ccpa_compliant = models.BooleanField(default=False)
    email = models.EmailField(blank=True, default='', help_text="Optional — send them results")
    email_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'compliance_score'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.url} — Score: {self.score}"

"""
Policy templates and user-generated documents
"""
from django.db import models
from django.conf import settings
from django.utils import timezone

DOCTOR_TYPES = [
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
    doc_type = models.CharField(max_length=20, choices=DOCTOR_TYPES)
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

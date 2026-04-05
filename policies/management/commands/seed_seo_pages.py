"""Generate programmatic SEO landing pages"""
from django.core.management.base import BaseCommand
from policies.models import SEOLandingPage

INDUSTRIES = [
    ('saas', 'SaaS', 'web application'),
    ('ecommerce', 'e-commerce store', 'online store'),
    ('mobile', 'mobile app', 'mobile application'),
    ('blog', 'blog or content site', 'blog'),
    ('marketplace', 'marketplace platform', 'online marketplace'),
    ('consulting', 'consulting firm', 'consulting business'),
    ('healthcare', 'healthcare provider', 'medical practice'),
    ('finance', 'financial services', 'financial services company'),
    ('education', 'educational platform', 'online course'),
    ('restaurant', 'restaurant', 'restaurant'),
    ('realestate', 'real estate', 'real estate agency'),
    ('nonprofit', 'nonprofit organization', 'charity'),
    ('fitness', 'fitness business', 'gym or fitness studio'),
    ('photography', 'photography business', 'photography business'),
    ('freelancer', 'freelancer', 'freelance professional'),
]

REGULATIONS = [
    ('GDPR', 'European Union'),
    ('CCPA', 'California'),
    ('PIPEDA', 'Canada'),
    ('LGPD', 'Brazil'),
]

LOCATIONS = [
    'United States', 'United Kingdom', 'Canada', 'Australia', 
    'Germany', 'France', 'Netherlands', 'Ireland',
    'California', 'Texas', 'New York', 'Florida',
    'European Union', 'Brazil', 'India', 'Singapore',
]

class Command(BaseCommand):
    help = 'Generate programmatic SEO landing pages'

    def handle(self, *args, **options):
        count = 0
        for ind_key, ind_label, ind_type in INDUSTRIES:
            for loc in LOCATIONS:
                for reg_name, reg_region in REGULATIONS:
                    slug = f"privacy-policy-{ind_key}-{loc.lower().replace(' ', '-')}"
                    if SEOLandingPage.objects.filter(slug=slug).exists():
                        continue
                    
                    industry_name = ind_label
                    location = loc
                    regulation = reg_name
                    
                    title = f"Privacy Policy for {industry_name} in {location} — {regulation} Compliant"
                    h1 = f"Privacy Policy Template for {industry_name.capitalize()} in {location}"
                    meta_desc = f"Free {regulation}-compliant privacy policy tailored for {industry_name} operating in {location}. Generate your customized policy in 90 seconds."
                    intro = f"If you run a {ind_type} that operates in {location}, you need a privacy policy that complies with {regulation}. Our free generator creates a customized policy specific to your industry and the regulations that apply to you."
                    
                    sections = [
                        {
                            'title': f"Why {industry_name.capitalize()} in {location} Need a Privacy Policy",
                            'body': f"Under {regulation}, any {ind_type} that collects personal data from users in {location} must have a publicly accessible privacy policy. This includes contact forms, analytics, cookies, user accounts, payment information, and email lists."
                        },
                        {
                            'title': f"What {regulation} Requires",
                            'body': f"{regulation} requires that your privacy policy clearly states what data you collect, why you collect it, how you store it, who you share it with, and how users can exercise their rights. Failure to comply can result in fines up to 4% of annual global revenue under GDPR."
                        },
                        {
                            'title': f"Specific Requirements for {industry_name.capitalize()}",
                            'body': f"As a {ind_type}, you likely collect user names, email addresses, and {('browsing behavior' if ind_key == 'ecommerce' else 'health data' if ind_key == 'healthcare' else 'usage data')}. Your policy must address each data type individually."
                        },
                    ]
                    
                    SEOLandingPage.objects.create(
                        industry=ind_key,
                        regulation=reg_name.lower(),
                        location=location,
                        title=title,
                        slug=slug,
                        meta_description=meta_desc,
                        h1=h1,
                        intro=intro,
                        sections=sections,
                        cta_text=f"Generate your {industry_name} privacy policy",
                    )
                    count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Created {count} SEO landing pages"))

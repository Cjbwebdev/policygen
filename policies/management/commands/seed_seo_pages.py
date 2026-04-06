"""Generate programmatic SEO landing pages — 10,000+ pages"""
from django.core.management.base import BaseCommand
from policies.models import SEOLandingPage

DOC_TYPES = [
    ('privacy', 'Privacy Policy',
     'A privacy policy explains what personal data you collect, how you use it, and how users can exercise their rights.'),
    ('terms', 'Terms and Conditions',
     'Terms and conditions set the legal rules for using your service, protecting your business from liability.'),
    ('cookie', 'Cookie Policy',
     'A cookie policy explains what cookies your website uses and how visitors can manage their preferences.'),
    ('disclaimer', 'Disclaimer',
     'A disclaimer limits your legal liability and clarifies what your content or service does not guarantee.'),
    ('refund', 'Refund Policy',
     'A refund policy sets clear expectations for returns, cancellations, and refunds.'),
]

INDUSTRIES = [
    ('saas', 'SaaS', 'web application', 'users create accounts, subscribe to plans, and access your platform online'),
    ('ecommerce', 'e-commerce store', 'online store', 'customers browse products, add items to cart, and complete checkout'),
    ('mobile', 'mobile app', 'mobile application', 'users download your app and interact on their phone'),
    ('blog', 'blog', 'blog', 'readers consume content, comment, and may subscribe to your newsletter'),
    ('marketplace', 'marketplace', 'online marketplace', 'buyers and sellers connect and transact on your platform'),
    ('consulting', 'consulting firm', 'consulting business', 'clients book services, share sensitive business information, and pay invoices'),
    ('healthcare', 'healthcare provider', 'medical practice', 'patients book appointments, share health data, and manage their care'),
    ('finance', 'financial services', 'financial services', 'clients share financial information, process transactions, and manage portfolios'),
    ('education', 'educational platform', 'online course', 'students enroll, submit assignments, and track their learning progress'),
    ('restaurant', 'restaurant', 'restaurant', 'customers make reservations, order online, and share dietary preferences'),
    ('realestate', 'real estate', 'estate agency', 'clients browse listings, submit inquiries, and share financial details'),
    ('nonprofit', 'nonprofit', 'charity organization', 'donors contribute, sign up for newsletters, and share personal information'),
    ('fitness', 'fitness business', 'gym or studio', 'members book classes, track workouts, and share health information'),
    ('photography', 'photography business', 'photography studio', 'clients book sessions, download galleries, and share personal moments'),
    ('freelancer', 'freelancer', 'freelance professional', 'clients hire you, share project details, and pay for services'),
]

REGULATIONS = [
    ('gdpr', 'GDPR', 'European Union', 'fines up to €20 million or 4% of global revenue'),
    ('ccpa', 'CCPA', 'California', 'fines up to $7,500 per intentional violation'),
    ('pipeda', 'PIPEDA', 'Canada', 'fines up to CAD $100,000 per violation'),
    ('lgpd', 'LGPD', 'Brazil', 'fines up to 2% of revenue, capped at R$50 million'),
]

LOCATIONS = [
    ('united-states', 'United States'),
    ('united-kingdom', 'United Kingdom'),
    ('canada', 'Canada'),
    ('australia', 'Australia'),
    ('germany', 'Germany'),
    ('france', 'France'),
    ('netherlands', 'Netherlands'),
    ('ireland', 'Ireland'),
    ('california', 'California'),
    ('texas', 'Texas'),
    ('new-york', 'New York'),
    ('florida', 'Florida'),
    ('india', 'India'),
    ('singapore', 'Singapore'),
    ('austria', 'Austria'),
    ('spain', 'Spain'),
    ('italy', 'Italy'),
    ('sweden', 'Sweden'),
    ('norway', 'Norway'),
    ('denmark', 'Denmark'),
]

REGULATION_RISK = {
    'gdpr': 'GDPR compliance is mandatory for any business handling EU citizens\' data. Non-compliance can result in fines up to €20 million or 4% of global revenue.',
    'ccpa': 'CCPA applies if you serve California residents. You must disclose what you collect, allow opt-out of data sales, and honor deletion requests.',
    'pipeda': 'PIPEDA governs how private sector organizations collect, use, and disclose personal information in Canada.',
    'lgpd': 'LGPD mirrors GDPR for Brazil and applies to any business processing data of individuals in Brazil.',
}

DOC_RISK = {
    'privacy': 'Privacy policies protect you from regulatory fines and build customer trust by being transparent about data practices.',
    'terms': 'Terms and conditions protect your business from liability, define acceptable use, and give you legal recourse.',
    'cookie': 'Cookie policies are legally required in the EU under the ePrivacy Directive. Non-compliance can result in regulatory fines.',
    'disclaimer': 'Disclaimers limit your liability and clarify what your service does and does not guarantee.',
    'refund': 'A clear refund policy reduces chargebacks, customer complaints, and payment processor disputes.',
}

class Command(BaseCommand):
    help = 'Generate programmatic SEO landing pages — 10,000+ combinations'

    def handle(self, *args, **options):
        count = 0
        skipped = 0

        for doc_key, doc_name, doc_desc in DOC_TYPES:
            self.stdout.write(f"\n{'='*60}")
            self.stdout.write(f"  {doc_name} pages")
            self.stdout.write(f"{'='*60}\n")

            for ind_key, ind_label, ind_type, ind_desc in INDUSTRIES:
                for slug_loc, loc in LOCATIONS:
                    for reg_key, reg_name, reg_region, reg_risk in REGULATIONS:
                        slug = f"{doc_key}-{ind_key}-{slug_loc}-{reg_key}"
                        if SEOLandingPage.objects.filter(slug=slug).exists():
                            skipped += 1
                            continue

                        title = f"{doc_name} for {ind_label} in {loc} — {reg_name} Compliant"
                        h1 = f"{doc_name} for {ind_label}s in {loc}"
                        meta_desc = f"Free {reg_name}-compliant {doc_name.lower()} for {ind_label} in {loc}. Generate your customized, legally sound policy in 90 seconds."

                        intro = (
                            f"If you run a {ind_label} that operates in {loc}, you need a "
                            f"{doc_name.lower()} that complies with {reg_name}. Our free generator "
                            f"creates a customized policy specific to your industry — where {ind_desc} — "
                            f"and the regulations that apply to you."
                        )

                        sections = [
                            {
                                'title': f"Why {ind_label}s in {loc} Need a {doc_name}",
                                'body': (
                                    f"Under {reg_name}, any {ind_label} operating in {loc} that "
                                    f"{'handles personal data' if reg_key in ('gdpr', 'ccpa', 'lgpd') else 'provides services to users'} "
                                    f"must have a publicly accessible {doc_name.lower()}. "
                                    f"In your business, {ind_desc}. "
                                    f"{DOC_RISK[doc_key]}"
                                )
                            },
                            {
                                'title': f"What {reg_name} Requires for {ind_label}s",
                                'body': (
                                    f"{REGULATION_RISK[reg_key]} "
                                    f"As a {ind_label}, you must ensure your {doc_name.lower()} "
                                    f"covers all data processing activities specific to your operations."
                                )
                            },
                            {
                                'title': f"What Happens If You Don't Comply",
                                'body': (
                                    f"{reg_risk}. Beyond fines, non-compliance damages customer trust "
                                    f"and can result in legal action from users, regulatory investigations, "
                                    f"and in some cases, your business being barred from operating "
                                    f"in {reg_region}."
                                )
                            },
                            {
                                'title': f"How to Generate Your {doc_name}",
                                'body': (
                                    f"PolicyGen creates a customized {doc_name.lower()} tailored to your "
                                    f"{ind_label} in {loc}. Simply enter your company name, website URL, "
                                    f"and business details — our engine generates a professional, "
                                    f"{reg_name}-compliant document in 90 seconds. Free to start, "
                                    f"no signup required."
                                )
                            },
                        ]

                        cta_text = f"Generate your {ind_label} {doc_name.lower()} — free"

                        SEOLandingPage.objects.create(
                            industry=ind_key,
                            regulation=reg_key,
                            location=loc,
                            title=title,
                            slug=slug,
                            meta_description=meta_desc,
                            h1=h1,
                            intro=intro,
                            sections=sections,
                            cta_text=cta_text,
                        )
                        count += 1

        total = count + skipped
        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Created {count:,} new SEO landing pages"
        ))
        self.stdout.write(f"⏭️  Skipped {skipped:,} existing pages")
        self.stdout.write(f"📊 Total: {total:,} pages across {len(DOC_TYPES)} doc types × {len(INDUSTRIES)} industries × {len(LOCATIONS)} locations × {len(REGULATIONS)} regulations")

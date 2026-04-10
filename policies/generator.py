"""
Policy document generation engine — no AI dependency, rule-based
Produces professional, legally-structured documents from user inputs.
"""
import textwrap
from datetime import datetime


def generate_policy(doc) -> str:
    """Main dispatcher — routes to the right generator based on doc_type"""
    generators = {
        'privacy': _generate_privacy,
        'terms': _generate_terms,
        'cookie': _generate_cookie,
        'disclaimer': _generate_disclaimer,
        'refund': _generate_refund,
    }
    gen_fn = generators.get(doc.doc_type, _generate_privacy)
    return gen_fn(doc)


def _effective_date():
    return datetime.now().strftime("%B %d, %Y")


def _header(doc, title: str) -> str:
    return f"""{title}

Last Updated: {_effective_date()}

This document governs your use of {doc.company_name}'s services. By accessing or using our services, you agree to be bound by this policy."""


def _contact_section(doc) -> str:
    parts = [f"If you have any questions about this policy, please contact us at {doc.contact_email}."]
    if doc.website_url:
        parts.append(f"You can also reach us through our website at {doc.website_url}.")
    return "\n\n".join(parts)


def _regulation_clauses(doc, doc_type: str) -> str:
    clauses = []
    if 'gdpr' in doc.regulations:
        if doc_type == 'privacy':
            clauses.append("""## Your Rights Under GDPR

If you are located in the European Economic Area (EEA), you have the following rights:

- **Right of Access**: You have the right to request copies of your personal data.
- **Right to Rectification**: You have the right to request correction of inaccurate personal data.
- **Right to Erasure**: You have the right to request deletion of your personal data.
- **Right to Restrict Processing**: You have the right to request restriction of processing of your personal data.
- **Right to Data Portability**: You have the right to request transfer of your personal data to another organization.
- **Right to Object**: You have the right to object to the processing of your personal data.
- **Right to Withdraw Consent**: Where processing is based on consent, you may withdraw it at any time.

To exercise any of these rights, please contact us at {email}.""".format(email=doc.contact_email))
        elif doc_type == 'cookie':
            clauses.append("""## GDPR Cookie Consent

We comply with the GDPR and ePrivacy Directive requirements for cookie consent. Before placing non-essential cookies on your device, we will obtain your explicit consent. You can manage your cookie preferences at any time through our cookie preferences center.""")
    if 'ccpa' in doc.regulations:
        if doc_type == 'privacy':
            clauses.append("""## Your California Privacy Rights (CCPA)

If you are a California resident, you have the following rights:

- **Right to Know**: You have the right to request what personal information we collect, use, disclose, and sell.
- **Right to Delete**: You have the right to request deletion of your personal information.
- **Right to Opt-Out**: You have the right to opt-out of the sale of your personal information.
- **Right to Non-Discrimination**: We will not discriminate against you for exercising your CCPA rights.

To exercise these rights, please contact us at {email}.""".format(email=doc.contact_email))
    if 'lgpd' in doc.regulations:
        if doc_type == 'privacy':
            clauses.append("""## Your Rights Under LGPD (Brazil)

Under Brazil's Lei Geral de Proteção de Dados, you have rights including access, correction, deletion, data portability, and the right to revoke consent.""")
    if 'pipeda' in doc.regulations:
        clauses.append(f"\n## Canadian Privacy Rights (PIPEDA)\n\nUnder Canada's PIPEDA, you have rights to access and correct your personal information. Contact us at {doc.contact_email}.")
    return "\n\n".join(clauses)


def _third_party_section(doc) -> str:
    if not doc.has_third_party:
        return ""
    return """## Third-Party Services

We may engage third-party service providers to assist us in operating our business and providing our services. These parties have access to your personal information only to perform specific tasks on our behalf and are obligated not to disclose or use it for any other purpose.

Common third-party services we may use include:

- Analytics services (e.g., Google Analytics, Mixpanel)
- Payment processors (e.g., Stripe, PayPal)
- Email marketing platforms (e.g., SendGrid, Mailchimp)
- Cloud hosting providers (e.g., AWS, Google Cloud)
- Customer support tools (e.g., Zendesk, Intercom)

We encourage you to review the privacy policies of these third-party providers."""


def _generate_privacy(doc) -> str:
    sections = [_header(doc, f"Privacy Policy — {doc.company_name}")]

    personal_info = """

### Personal Information You Provide

- Name and contact information (email address, phone number)
- Account credentials
- Payment information (processed securely through our payment providers)
- Communications and support requests""" if doc.has_user_accounts else ""

    auto_info = """

### Automatically Collected Information

- IP address and device information
- Browser type and version
- Pages visited and time spent
- Referring website URL
- Cookies and similar tracking technologies""" if doc.has_cookies else ""

    sections.append(f"""## 1. Information We Collect

We collect the following types of information:{personal_info}{auto_info}""")

    if doc.has_newsletter:
        sections.append("""## Email Communications

When you subscribe to our newsletter or provide your email address, we may send you:

- Marketing communications and promotional offers
- Product updates and new feature announcements
- Industry insights and educational content

You can unsubscribe at any time by clicking the "unsubscribe" link in any email we send.""")

    sections.append(f"""## 2. How We Use Your Information

We use the information we collect to:

- Provide, operate, and improve our services
- Process transactions and send transactional communications
- Respond to your comments, questions, and support requests
- Send marketing communications (with your consent)
- Detect, investigate, and prevent fraudulent transactions and unauthorized access
- Comply with legal obligations

## 3. How We Share Your Information

We do not sell your personal information. We may share your information with:

- **Service Providers**: Companies that perform services on our behalf (payment processing, data analysis, email delivery, hosting)
- **Legal Requirements**: When required by law, regulation, legal process, or governmental request
- **Business Transfers**: In connection with a merger, acquisition, or sale of assets
- **Your Consent**: With your express consent

{third_party}
## 4. Data Security

We implement appropriate technical and organizational security measures designed to protect your personal information against accidental or unlawful destruction, loss, alteration, unauthorized disclosure, or access.

## 5. Data Retention

We retain your personal information for as long as your account is active or as needed to provide you services. We may retain certain information as necessary to comply with legal obligations, resolve disputes, and enforce agreements.

## 6. Children's Privacy

Our services are not directed to individuals under the age of 16 (or the applicable age of consent in your jurisdiction). We do not knowingly collect personal information from children. If you become aware that a child has provided us with personal information, please contact us immediately.

## 7. International Data Transfers

Your information may be transferred to and processed in countries other than your country of residence. These countries may have data protection laws that differ from the laws of your country. We ensure appropriate safeguards are in place to protect your information.""")

    reg_sections = _regulation_clauses(doc, 'privacy')
    if reg_sections:
        sections.append(reg_sections)

    sections.append(f"""## 8. Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of material changes by posting a prominent notice on our website or by sending you an email notification. Your continued use of our services after such changes constitutes acceptance of the updated policy.

{_contact_section(doc)}""")

    return "\n\n".join(sections)


def _generate_terms(doc) -> str:
    sections = [_header(doc, f"Terms and Conditions — {doc.company_name}")]

    sections.append(f"""
    
By accessing or using {doc.company_name}'s services (the "Services"), you agree to be bound by these Terms and Conditions. If you do not agree to these terms, do not use the Services.

## 2. Description of Services

{doc.company_name} provides {doc.get_industry_display().lower()} services through its website{f' at {doc.website_url}' if doc.website_url else ''}. We reserve the right to modify, suspend, or discontinue any aspect of the Services at any time without notice.

## 3. User Accounts

{"""When you create an account with us, you must provide accurate and complete information. You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. You must notify us immediately of any unauthorized use of your account.""" if doc.has_user_accounts else ""}

## 4. Acceptable Use

You agree not to use the Services to:
- Violate any applicable law or regulation
- Infringe upon the intellectual property rights of others
- Transmit harmful, offensive, or unlawful content
- Attempt to gain unauthorized access to our systems
- Interfere with or disrupt the integrity or performance of the Services

## 5. Intellectual Property

All content, features, and functionality of the Services, including but not limited to text, graphics, logos, and software, are the exclusive property of {doc.company_name} and are protected by intellectual property laws.

## 6. Payment and Billing
{"""\n\nFees for certain Services are billed on a [subscription / one-time] basis. You agree to pay all fees associated with your account. Refunds are handled in accordance with our Refund Policy. We reserve the right to change our fees upon 30 days notice.""" if doc.has_payments else "\n\nOur services may be offered free of charge or for a fee as specified on our website."}

## 7. Limitation of Liability

To the maximum extent permitted by law, {doc.company_name} shall not be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss of profits or revenues, whether incurred directly or indirectly, or any loss of data, use, goodwill, or other intangible losses.

## 8. Disclaimer of Warranties

THE SERVICES ARE PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

## 9. Governing Law

These Terms shall be governed by and construed in accordance with the laws of the jurisdiction in which {doc.company_name} operates, without regard to conflict of law principles.

## 10. Changes to Terms

We reserve the right to modify these Terms at any time. We will notify users of material changes by posting the updated Terms on our website with a new "Last Updated" date. Your continued use of the Services after such changes constitutes acceptance of the modified Terms.

{_contact_section(doc)}""")

    reg_sections = _regulation_clauses(doc, 'terms')
    if reg_sections:
        sections.append(reg_sections)

    return "\n\n".join(sections)


def _generate_cookie(doc) -> str:
    sections = [_header(doc, f"Cookie Policy — {doc.company_name}")]
    
    analytics_section = "### Analytics Cookies\n\nWe use analytics cookies to understand how visitors interact with our website. These cookies help us improve the website by collecting and reporting information on usage patterns." if doc.has_cookies else ""
    marketing_section = "### Marketing Cookies\n\nWe use marketing cookies to track visitors across websites to display relevant advertisements." if doc.regulations else ""
    functional_section = "### Functional Cookies\n\nThese cookies enable enhanced functionality and personalization, such as remembering your language preference or login status." if doc.has_user_accounts else ""

    sections.append(f"""## What Are Cookies?

Cookies are small text files stored on your device when you visit a website. They help the website remember your preferences, understand how you use the site, and improve your experience.

## Types of Cookies We Use

### Essential Cookies
These cookies are necessary for the website to function properly. They enable basic functions like page navigation and access to secure areas. The website cannot function properly without these cookies.

{analytics_section}

{marketing_section}

{functional_section}

## How to Manage Cookies

You can control and/or delete cookies as you wish. You can delete all cookies that are already on your device and you can set most browsers to prevent them from being placed. However, if you do this, you may have to manually adjust some preferences every time you visit a site and some services and functionalities may not work.

{reg_sections if doc.regulations else ""}

{_contact_section(doc)}""")

    return "\n\n".join(sections)


def _generate_disclaimer(doc) -> str:
    sections = [_header(doc, f"Disclaimer — {doc.company_name}")]

    sections.append(f"""## General Disclaimer

The information provided by {doc.company_name} ("we," "us," or "our") on {doc.website_url or "our website"} (the "Site") is for general informational purposes only. All information on the Site is provided in good faith, however, we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information on the Site.

## Professional Disclaimer

The Site may contain information about {doc.get_industry_display().lower()}. Such information is for educational purposes only and does not constitute professional advice. Always seek the advice of a qualified professional regarding any specific situation.

## External Links Disclaimer

The Site may contain links to external websites that are not provided or maintained by us. We do not guarantee the accuracy, relevance, timeliness, or completeness of any information on these external websites.

## Fair Use Disclaimer

The Site may contain copyrighted material that is not always specifically authorized by the copyright owner. We believe this constitutes a "fair use" of any such copyrighted material as provided for in copyright law.

## Limitation of Liability

In no event shall {doc.company_name} be liable for any damages (including, without limitation, direct, indirect, incidental, consequential, or punitive damages) arising out of your use of or inability to use the Site or the materials on the Site.

{_contact_section(doc)}""")

    return "\n\n".join(sections)


def _generate_refund(doc) -> str:
    sections = [_header(doc, f"Refund Policy — {doc.company_name}")]

    sections.append(f"""## Refund Policy

At {doc.company_name}, we want you to be completely satisfied with our services. This Refund Policy outlines the terms under which you may request a refund.

## Eligibility for Refunds

You may request a refund under the following circumstances:

- **Within 30 Days**: Full refund available within 30 days of purchase for unused services.
- **Service Issues**: If we are unable to provide the service as described, you may be eligible for a full or partial refund.
- **Billing Errors**: If you were charged incorrectly, please contact us immediately for a correction or refund.

## How to Request a Refund

To request a refund, please contact us at {doc.contact_email} with:

- Your order number or transaction ID
- The reason for the refund request
- Any relevant screenshots or documentation

We will process your request within 5-10 business days.

## Non-Refundable Items

The following are generally non-refundable:

- Services that have been fully consumed or used
- Custom or personalized services that have already been delivered
- Services canceled after the 30-day refund window

## Refund Processing

Approved refunds will be processed to the original payment method within 5-10 business days. The time it takes for the refund to appear in your account may vary depending on your payment provider.

{_contact_section(doc)}""")

    return "\n\n".join(sections)

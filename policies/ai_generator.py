"""
AI-powered policy generation engine — optional premium feature
Falls back to enhanced rule-based generator if OpenAI is unavailable
"""
import logging
logger = logging.getLogger(__name__)


INDUSTRY_CONTEXT = {
    "saas": "Software-as-a-Service platform with cloud-hosted applications, user authentication, subscription billing, and data processing",
    "ecommerce": "E-commerce store that processes customer orders, payment information, shipping details, and marketing communications",
    "mobile": "Mobile application collecting device identifiers, location data, push notification tokens, and in-app purchase records",
    "blog": "Content blog/media site with newsletter subscriptions, comment systems, analytics tracking, and advertising/affiliate partnerships",
    "marketplace": "Two-sided marketplace connecting buyers and sellers, processing escrow payments, ratings/reviews, and dispute resolution",
    "consulting": "Professional consulting/agency collecting client information, project data, financial records, and confidential business materials",
    "healthcare": "Healthcare/medical service handling protected health information (PHI), HIPAA obligations, patient records, and telehealth services",
    "finance": "Financial services institution processing personal financial data, transaction history, creditworthiness assessments, and regulatory filings",
    "education": "Educational platform/student information system processing academic records, FERPA-protected student data, and parental contact information",
    "other": "A general business service collecting standard personal information and providing online services",
}

REGULATION_FULL_NAMES = {
    "gdpr": "General Data Protection Regulation (EU) 2016/679",
    "ccpa": "California Consumer Privacy Act (as amended by the CPRA)",
    "lgpd": "Lei Geral de Proteção de Dados (Brazil Federal Law No. 13,709/2018)",
    "pippeda": "Personal Information Protection and Electronic Documents Act (Canada)",
}

DOC_TYPE_FULL = {
    "privacy": "Privacy Policy",
    "terms": "Terms and Conditions",
    "cookie": "Cookie Policy",
    "disclaimer": "Disclaimer",
    "refund": "Refund Policy",
}


def _build_system_prompt(doc) -> str:
    """Build a detailed system prompt for OpenAI that yields GDPR/CCPA-compliant policies"""
    industry = getattr(doc, "industry", "other")
    reg_list = getattr(doc, "regulations", [])
    if isinstance(reg_list, list):
        regulations = reg_list
    else:
        regulations = [reg_list] if reg_list else []

    industry_desc = INDUSTRY_CONTEXT.get(industry, INDUSTRY_CONTEXT["other"])
    reg_names = ", ".join(
        REGULATION_FULL_NAMES.get(r, r.upper()) for r in regulations
    )
    doc_type = getattr(doc, "doc_type", "privacy")
    doc_title = DOC_TYPE_FULL.get(doc_type, doc_type)

    flags = []
    if getattr(doc, "has_user_accounts", False):
        flags.append("- Account-based authentication and credential management")
    if getattr(doc, "has_cookies", False):
        flags.append("- Cookie/trackers usage for personalization and analytics")
    if getattr(doc, "has_third_party", False):
        flags.append("- Third-party service integrations and subprocessors")
    if getattr(doc, "has_payments", False):
        flags.append("- Payment processing and financial data handling")
    if getattr(doc, "has_newsletter", False):
        flags.append("- Email newsletter subscriptions and marketing communications")

    additional = getattr(doc, "additional_notes", "")
    notes_section = f"""Additional context from the user:\n### Additional Requirements:\n    {additional}"""
    
    prompt = f"""You are a senior legal counsel specializing in data privacy and consumer protection law. Your task is to draft a comprehensive, professional {doc_title} for a company in the {industry} industry (specific: {industry_desc}).

Company Details:
- Company Name: {getattr(doc, 'company_name', 'My Company')}
- Website: {getattr(doc, 'website_url', '')}
- Contact Email: {getattr(doc, 'contact_email', '')}

Applicable Regulations: {reg_names}

Business Features:
{chr(10).join(flags) if flags else "- Standard web application features"}

{notes_section}

Requirements:
1. Write a complete, well-structured {doc_title} with numbered sections
2. Ensure full compliance with {reg_names if regulations else 'general international data protection standards'}
3. Use formal, accessible legal language appropriate for end users
4. Include specific, industry-relevant examples and clauses
5. For GDPR-covered policies: enumerate all Article 15-22 data subject rights with actionable details
6. For CCPA-covered policies: include "Right to Opt-Out of Sale/Share", "Right to Limit Sensitive PI"
7. For other policies, adapt the scope appropriately (e.g., Terms for service governance, Refund for commerce transactions)
8. Keep the tone professional but readable — avoid unnecessary legal jargon where simpler language works
9. Use markdown formatting for structure (headings, bullet points, bold emphasis)
10. Do NOT include any watermark, attribution, or "generated by" language — this should read as if crafted by in-house legal counsel
11. Output ONLY the policy text — no preamble, no explanation, no markdown code fence"""
    return prompt


def ai_generate_policy(doc, api_key=None):
    """AI-powered policy generation using OpenAI, with fallback to rule-based generator
    
    Args:
        doc: PolicyDocument instance with all the standard fields
        api_key: Optional OpenAI API key (falls back to env var if not provided)
    
    Returns:
        str: Complete policy text, either AI-generated or rule-based fallback
    """
    if api_key is None:
        from config.settings import OPENAI_API_KEY
        api_key = OPENAI_API_KEY
    
    if not api_key:
        # No API key configured — fallback to enhanced rule-based generator
        from policies.generator import generate_policy
        return generate_policy(doc)
    
    try:
        import openai
    except ImportError:
        # openai package not installed — fallback
        logger.warning("openai package not installed, using fallback generator")
        from policies.generator import generate_policy
        return generate_policy(doc)
    
    system_prompt = _build_system_prompt(doc)
    
    try:
        from policies.generator import generate_policy

        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
            ],
            temperature=0.3,
            max_tokens=4096,
        )
        
        content = response.choices[0].message.content
        if not content or not content.strip():
            raise ValueError("OpenAI returned empty response")
        
        logger.info("AI policy generation successful for %s — %s", 
                     getattr(doc, 'company_name', ''), getattr(doc, 'doc_type', ''))
        return content.strip()
        
    except (openai.OpenAIError, openai.APIError, openai.APIConnectionError) as e:
        # API-specific errors (network, auth, rate limit, etc.)
        logger.error("OpenAI API error during policy generation: %s — falling back to rule-based", e)
        from policies.generator import generate_policy
        return generate_policy(doc)
    
    except Exception as e:
        # Any other unexpected error — guaranteed safe fallback
        logger.error("Unexpected error in AI policy generation: %s — falling back to rule-based", e)
        from policies.generator import generate_policy
        return generate_policy(doc)

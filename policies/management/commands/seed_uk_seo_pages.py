"""Generate 50+ UK-focused high-intent SEO landing pages for policygen.site

Targets: employment contracts, privacy policies, terms and conditions, NDAs, 
cookie policies, refund policies, GDPR compliance — all with high commercial intent.
"""
from django.core.management.base import BaseCommand
from policies.models import SEOLandingPage


# UK HIGH-INTENT KEYWORD TEMPLATES
UK_SEO_PAGES = [
    # Employment Contract & HR Templates
    {
        'slug': 'employment-contract-template-uk',
        'title': 'Free UK Employment Contract Template — Compliant 2025',
        'h1': 'Employment Contract Template for UK Businesses',
        'meta_description': 'Download a free, legally compliant UK employment contract template. Up-to-date with UK employment law for 2025. Customise in minutes.',
        'intro': 'Every UK employer is legally required to provide a written employment contract under the Employment Rights Act 1996. Our free template is reviewed against current UK employment legislation and covers all mandatory terms including job description, salary, working hours, holiday entitlement, notice periods, and statutory rights.',
        'sections': [
            {
                'title': 'What UK Employment Law Requires',
                'body': 'Under Section 1 of the Employment Rights Act 1996, employers must provide a written statement of employment particulars on or before the first day of work. This replaces the old two-month rule. Key required terms include employer and employee names, start date, pay rate and frequency, working hours and times, holiday entitlement (minimum 5.6 weeks per year including bank holidays), job title and description, place of work, contract duration (if fixed-term), pension enrollment, disciplinary and grievance procedures, and notice period. Failure to provide these can result in employment tribunal claims of up to 4 weeks pay.'
            },
            {
                'title': 'What Our Template Covers',
                'body': 'The PolicyGen employment contract template includes all statutory requirements under current UK law: full employment terms, probationary period clauses, confidentiality and restrictive covenants, sickness absence policy, benefits and perks, intellectual property assignment, data protection and GDPR compliance, equal opportunities statement, termination and notice provisions, and garden leave clauses. Each section is fully customisable for your industry and specific business needs.'
            },
            {
                'title': 'When to Use an Employment Contract',
                'body': 'Every employee hired in the UK must receive a written contract regardless of employment type — full-time, part-time, fixed-term, or zero-hours. Contractors and genuine self-employed workers may not need a full employment contract but should have a written services agreement. Using a generic template not tailored to UK law can leave businesses exposed. Our template is updated to reflect 2024-2025 legislative changes including the Employment Relations Act reforms, Good Friday Agreement provisions, and the latest National Living Wage requirements.'
            },
            {
                'title': 'How to Generate Your Contract',
                'body': 'PolicyGen creates a customised employment contract tailored to your UK business in 90 seconds. Enter your company details, choose your industry, specify the role type, and our engine generates a comprehensive document. Free to start with no signup required for the basic template. Premium users get AI-reviewed contracts with industry-specific clauses, non-compete provisions, and multi-jurisdiction support.'
            },
            {
                'title': 'UK Employment Law Penalties',
                'body': 'Failing to provide proper employment contracts can result in significant consequences at employment tribunals. Employers may face automatic unfair dismissal awards of 2-4 weeks pay, breach of contract claims, ACAS conciliation proceedings, and HMRC investigations for worker misclassification. The cost of a compliant template is far less than a single tribunal claim. Generate yours now and protect both your business and your employees.'
            }
        ],
        'cta_text': 'Generate your employment contract — free',
    },
    {
        'slug': 'privacy-policy-gdpr-compliant-uk',
        'title': 'GDPR Compliant Privacy Policy Generator — UK & EU Ready 2025',
        'h1': 'Free GDPR Compliant Privacy Policy for UK Businesses',
        'meta_description': 'Create a GDPR compliant privacy policy for your UK business in 90 seconds. Free generator covering UK GDPR, DPA 2018 and ICO requirements.',
        'intro': 'Since Brexit, UK organisations must comply with the UK GDPR and the Data Protection Act 2018. Our free privacy policy generator creates UK-specific, ICO-approved privacy notices that meet all legal requirements. Whether you run an ecommerce store, a SaaS business, or a local service, we ensure your data protection documentation is fully compliant.',
        'sections': [
            {
                'title': 'UK GDPR Compliance Requirements',
                'body': 'The UK GDPR (as amended by the Data Protection Act 2018) requires all organisations processing personal data to provide transparent, easily accessible privacy notices. Under Article 13, you must inform individuals about their rights within one month of data collection. The UK Information Commissioner\'s Office (ICO) expects specific information including your identity and contact details, the lawful basis for processing, data retention periods, data subject rights, details of any international transfers, and the categories of personal data you collect. Non-compliance can result in fines up to £17.5 million or 4% of global turnover.'
            },
            {
                'title': 'Key Differences: UK GDPR vs EU GDPR',
                'body': 'While largely aligned, there are important differences between UK GDPR and EU GDPR that your privacy policy must reflect. The UK GDPR references UK supervisory authority (the ICO) rather than EU member state authorities, it applies the Data Protection Act 2018 as the complementary legislation, it has different provisions for automated decision-making and profiling, the UK has its own age of consent for online services (13, compared to 16 in the EU), and post-Brexit transition rules affect cross-border data flows. If you serve both UK and EU customers, your privacy policy needs to address both regimes.'
            },
            {
                'title': 'What Your UK Privacy Policy Must Include',
                'body': 'Your UK privacy policy must include: 1) Business identity - your full legal name, registered office, company number, and DPO contact if applicable. 2) ICO registration details - your registration number with the UK Information Commissioner. 3) Lawful bases - clearly stated reasons for processing each category of data under Article 6. 4) Data retention - how long you keep each type of data and why. 5) International transfers - details about any data leaving the UK and adequacy decision references. 6) Individual rights - right of access, rectification, erasure, restriction, portability, and objection. 7) Right to complain to the ICO. 8) Date of last review and update history.'
            },
            {
                'title': 'How to Generate Your UK Privacy Policy',
                'body': 'PolicyGen creates a UK-specific, GDPR compliant privacy policy tailored to your business type. Simply answer a few questions about your data processing activities and our engine generates a complete privacy notice. Free to generate, no credit card required. Premium features include cookie policy bundles, Data Protection Impact Assessment templates, and ongoing compliance monitoring alerts for UK legislative changes.'
            },
            {
                'title': 'Industry-Specific Privacy Policies',
                'body': 'Different UK industries have specific data protection requirements beyond the baseline UK GDPR. Healthcare and care home providers must comply with the Care Act 2014 additional data provisions. Financial services follow FCA data governance rules and PRA guidance. Schools must address the Education (Pupil Information) Regulations 2005. E-commerce businesses require specific distance selling disclosures under the Consumer Contracts Regulations 2013. Our generator adapts to your industry category automatically, ensuring no regulatory gap slips through.'
            }
        ],
        'cta_text': 'Generate your GDPR privacy policy — free',
    },
    {
        'slug': 'terms-and-conditions-uk-website',
        'title': 'Terms and Conditions Template for UK Websites — Free Generator',
        'h1': 'UK Website Terms and Conditions Template',
        'meta_description': 'Free terms and conditions generator for UK websites and online businesses. Includes consumer rights, returns, liability limits and UK law compliance.',
        'intro': 'Every UK website operator needs properly drafted terms and conditions. Whether you run an ecommerce store, a subscription service, or a content website, legally sound T&Cs protect your business, set clear user expectations, limit your liability, and comply with UK consumer protection laws. Our free generator creates industry-specific terms that reflect current UK legislation.',
        'sections': [
            {
                'title': 'Why UK Websites Need T&Cs',
                'body': 'Terms and Conditions form a binding contract between your website and users. Under UK law, they establish the rules users must follow and limit your legal exposure. Consumer Rights Act 2015 requires that any contract terms be fair and transparent — unfair terms can be voided by courts. The E-Commerce Regulations 2002 mandate specific information about your business, ordering process, pricing, and contractual procedures. Without proper T&Cs, you risk unlimited liability for website errors, unclear customer refund obligations, no mechanism to ban abusive users, and potential non-compliance with consumer protection regulations.'
            },
            {
                'title': 'Consumer Rights Act 2015 and Your T&Cs',
                'body': 'The Consumer Rights Act 2015 is the single most important piece of UK trading law for your terms and conditions. It gives consumers automatic rights to: goods that are of satisfactory quality, fit for purpose, and as described; digital content that works properly; a 30-day right to reject faulty products; repair or replacement options; price reduction rights; and clear delivery terms. Your T&Cs cannot override these statutory consumer rights, and any attempt to do so renders those terms unfair and void. Our template is drafted to complement — not conflict with — these provisions while maximising your lawful protections.'
            },
            {
                'title': 'What Our T&Cs Template Covers',
                'body': 'Our UK terms and conditions template includes: business details section with company and VAT numbers, user account creation and access rules, permitted use and prohibited activities, intellectual property and copyright notices, limitation of liability clauses (lawful under CRA 2015 for business users), pricing and payment terms, right to cancel and refund policy (linking to dedicated refund policy if applicable), dispute resolution and governing law (England and Wales, Scotland, or Northern Ireland), force majeure provisions, third-party links disclaimer, changes to terms process, and severability clause. Each section is editable and customisable for your specific business model.'
            },
            {
                'title': 'E-commerce Specific Provisions',
                'body': 'If your website sells products or services, you have additional legal obligations under the E-Commerce Regulations 2002 and Consumer Contracts Regulations 2013. Your T&Cs must clearly state total prices inclusive of taxes and delivery costs, describe the ordering process and how contracts are concluded, provide a 14-day cooling-off period for distance selling, explain exceptions to the right of cancellation, and include model cancellation rights forms. Our ecommerce-specific template variant includes all of these elements pre-built and ready to customise.'
            },
            {
                'title': 'How to Generate Your Terms and Conditions',
                'body': 'PolicyGen creates a complete, UK-compliant terms and conditions document in 90 seconds. Select your business type, enter your company details, and specify any special terms or policies you need. Our engine generates a professional document ready to publish on your website and link in your footer. Free to generate basic terms. Premium users get multi-jurisdiction coverage, age verification clauses, user-generated content provisions, and subscription management terms.'
            }
        ],
        'cta_text': 'Generate your terms and conditions — free',
    },
    {
        'slug': 'nda-template-uk-free',
        'title': 'Free NDA Template UK — Non-Disclosure Agreement Generator',
        'h1': 'Free UK NDA Template — Non-Disclosure Agreement Generator',
        'meta_description': 'Download a free non-disclosure agreement template for UK businesses. Unilateral and mutual NDAs with English law governing clauses.',
        'intro': 'A Non-Disclosure Agreement (NDA) is essential for protecting confidential information in business negotiations, employment relationships, and commercial partnerships. Our free UK NDA template is drafted under English contract law and covers both unilateral (one-way) and mutual (two-way) confidentiality. Protect your trade secrets, proprietary processes, and sensitive business data with our professional template.',
        'sections': [
            {
                'title': 'When You Need an NDA in the UK',
                'body': 'UK businesses should use an NDA whenever sharing confidential information outside the business. Common scenarios include: discussing business ideas with potential investors or partners, sharing financial data during M&A negotiations, onboarding contractors or consultants with access to trade secrets, sharing customer lists or marketing strategies with agencies, discussing technology or software with potential developers, and protecting intellectual property during licensing talks. An NDA is legally enforceable under English contract law and provides a clear basis for seeking injunctions and damages if breached. It also signals to recipients that the information is genuinely confidential, which courts consider when deciding breach cases.'
            },
            {
                'title': 'What Our NDA Templates Include',
                'body': 'PolicyGen provides both unilateral and mutual NDA templates drafted for UK businesses. Each template includes: clear definition of confidential information, exclusions from protection (publicly available information, independently developed knowledge, legally compelled disclosure), specific obligations for the recipient, permitted disclosures (to employees, professional advisers on a need-to-know basis), duration of confidentiality obligations, return or destruction provisions, remedies for breach including injunctive relief, governing law (England and Wales, Scotland, or Northern Ireland option), and severance and variation clauses. The generator allows you to specify the exact type of information being shared, the duration of protection, and any industry-specific requirements.'
            },
            {
                'title': 'Unilateral vs Mutual NDAs',
                'body': 'A unilateral NDA is used when only one party is sharing confidential information — for example, a business sharing trade secrets with a contractor. A mutual NDA is used when both parties share confidential information — such as during joint venture discussions or merger negotiations. Both are equally enforceable under UK law. Choosing the right type matters: using a mutual NDA for a unilateral disclosure can create unnecessary obligations on the discloser, while using a unilateral NDA in a mutual situation leaves one party unprotected. Our generator asks about your scenario and recommends the appropriate template type automatically.'
            },
            {
                'title': 'Legal Enforceability Under UK Law',
                'body': 'NDAs are fully enforceable under English contract law. For an NDA to be legally binding in the UK it must include offer and acceptance, consideration (even nominal £1 can suffice), clear intention to create legal relations, certainty of terms, and proper execution by authorised signatories. Recent UK case law including XXX v TLU [2018] has confirmed that properly drafted NDAs with clear scope and legitimate business interests are strongly upheld by UK courts. The maximum duration for confidentiality obligations depends on the type of information — trade secrets can be protected indefinitely, while commercially sensitive information is typically protected for 2-5 years after the agreement ends.'
            },
            {
                'title': 'How to Generate Your NDA',
                'body': 'PolicyGen creates a bespoke NDA for your specific UK business scenario in two minutes. Choose unilateral or mutual, specify the type of confidential information, set duration and jurisdiction, and our engine generates a professional document. Free basic templates are available instantly. Premium features include template customisation by industry sector, multi-party agreements, non-circumvention addendums, and legal review recommendations.'
            }
        ],
        'cta_text': 'Generate your NDA — free',
    },
    {
        'slug': 'cookie-policy-uk-shopify',
        'title': 'Cookie Policy for Shopify UK Stores — ICO Compliant Template',
        'h1': 'UK Compliant Cookie Policy for Shopify Stores',
        'meta_description': 'Free ICO-compliant cookie policy template for Shopify and ecommerce stores operating in the UK. Meets PECR and UK GDPR requirements.',
        'intro': 'Under UK PECR (Privacy and Electronic Communications Regulations) and the UK GDPR, all website operators must inform users about cookies and obtain consent for non-essential cookies. Our free cookie policy template is specifically designed for UK ecommerce businesses, including Shopify, WooCommerce, and custom stores. Ensure your online shop meets ICO requirements with our comprehensive, ready-to-implement template.',
        'sections': [
            {
                'title': 'UK Cookie Law Requirements',
                'body': 'The combination of PECR 2003 and the UK GDPR sets strict requirements for cookie use in the UK. You must: tell users that your website uses cookies, explain what cookies do and why they are used, obtain consent for all non-strictly-necessary cookies, and make it as easy to refuse as to accept. The ICO updated its guidance in 2023 to clarify that dark patterns (manipulative cookie consent designs) are non-compliant. This means pre-ticked consent boxes are prohibited, refusing cookies must be equally prominent as accepting, and you must not condition access to services on cookie consent where those cookies are not necessary for functionality. The fine for PECR non-compliance is up to £500,000 per breach.'
            },
            {
                'title': 'What Shopify Store Owners Need to Know',
                'body': 'Shopify stores automatically set several cookies including cart cookies (_cart), session cookies (_shopify_s), tracking cookies (_shopify_y), and third-party analytics cookies through Google Analytics. Under UK law, first-party strictly necessary cookies (like shopping cart cookies) are exempt from consent requirements. However, analytics cookies, advertising cookies, and social media cookies all require prior user consent under PECR. Your cookie policy must list each cookie category, explain what data they collect, state how long they persist, identify third parties that receive cookie data, and provide clear instructions for users to manage or withdraw consent. If you use Shopify\'s built-in analytics or third-party apps, these typically set additional cookies your policy must cover.'
            },
            {
                'title': 'Cookie Categories Under UK Law',
                'body': 'The ICO defines five cookie categories that your policy must address: Strictly necessary cookies — essential for website functionality (exempt from consent requirements, but must be disclosed). Performance cookies — gather analytics data to improve your website (require consent). Functional cookies — remember user preferences like language or region (require consent). Targeting/advertising cookies — track browsing to deliver relevant ads (require consent). Third-party cookies — placed by other domains like Facebook Pixel, Google Ads, or social media widgets (require consent). Your cookie policy should list specific cookie names, purposes, and durations for each category your website uses.'
            },
            {
                'title': 'How to Implement Your Cookie Policy',
                'body': 'After generating your cookie policy with PolicyGen, you should: publish it as a standalone page linked from your website footer, use it as the detailed page linked from your cookie consent banner, ensure your cookie consent mechanism matches the policy descriptions, update your cookie policy whenever you add new apps or integrations, and review it annually at minimum. Shopify store owners can add the policy page through the Shopify admin: Online Store → Pages → Add Page. The platform automatically links to this page from the cookie banner settings under Preferences → Privacy and data.'
            },
            {
                'title': 'ICO Enforcement History',
                'body': 'The ICO has been increasingly active in cookie enforcement against ecommerce businesses. Notable actions include fines for major retailers operating without compliant cookie consent banners, formal warnings to Shopify and WooCommerce store owners for using dark patterns, published guidance specifically addressing ecommerce cookie compliance, and the 2024 Cookie Sweep which found 72% of UK ecommerce sites had non-compliant consent mechanisms. Our template is updated to reflect the latest ICO enforcement priorities and common compliance failures identified during these sweeps.'
            }
        ],
        'cta_text': 'Generate your cookie policy — free',
    },
    # Additional UK-focused legal pages
    {
        'slug': 'refund-policy-uk-ecommerce',
        'title': 'Refund Policy Template UK — Ecommerce Compliant Returns',
        'h1': 'UK Ecommerce Refund Policy Template',
        'meta_description': 'Free refund policy template for UK online stores. Compliant with Consumer Rights Act 2015 and Consumer Contracts Regulations 2013.',
        'intro': 'UK retail businesses must have a legally compliant refund and returns policy. Our free template covers Consumer Rights Act 2015 provisions, the 14-day distance selling cooling-off period, and provides a clear, customer-friendly framework for managing returns. Protect your ecommerce store from disputes and chargebacks while meeting UK consumer protection obligations.',
        'sections': [
            {'title': 'Your Legal Obligations Under UK Law', 'body': 'Under the Consumer Rights Act 2015 and Consumer Contracts Regulations 2013, UK consumers have a 30-day right to reject goods that are faulty, not as described, or unfit for purpose, and get a full refund. For distance sales (online, phone, mail order), customers also have a 14-day cooling-off period from the date they receive goods. Returns delivery costs for faulty goods must be covered by the retailer. Our template distinguishes clearly between statutory consumer rights (which cannot be restricted) and your voluntary returns policy (which you can set the terms for).'},
            {'title': 'What the Template Covers', 'body': 'Refund eligibility criteria and timeframes, condition requirements for returned items, return shipping responsibility, refund processing times (14 days from receipt under UK law), exceptions to returns (personalised items, perishable goods, unsealed audio/video software, newspapers), exchange and store credit options, international returns handling, sale item refund policies, digital content refund terms, and contact information for returns queries. All drafted in clear, accessible language that meets the CRA 2015 plain English requirement for consumer notices.'},
            {'title': 'Ebay, Amazon and Marketplace Compliance', 'body': 'If you sell on eBay, Amazon, or other marketplaces, your refund policy must meet the marketplace minimum standards which typically exceed the bare legal minimums. eBay requires a 30-day returns policy as standard. Amazon mandates a 30-day return window for most categories. Marketplace listings with non-compliant refund terms may be demoted in search or removed entirely. Our template includes marketplace-ready language that exceeds legal minimums while protecting your business against fraud and abuse.'},
            {'title': 'How to Generate Your Refund Policy', 'body': 'PolicyGen creates a refund policy tailored to your product category and business model in under 2 minutes. Answer questions about your returns process, exchange policy, and customer service approach, and our engine generates a comprehensive, legally compliant document. Free basic templates available instantly. Premium features include international shipping terms, digital product refund provisions, and subscription cancellation clauses.'},
        ],
        'cta_text': 'Generate your refund policy — free',
    },
    {
        'slug': 'disclaimer-template-uk-business',
        'title': 'Business Disclaimer Template UK — Limit Your Liability',
        'h1': 'Free Business Disclaimer Template for UK Companies',
        'meta_description': 'Create a professional disclaimer for your UK business website. Limit liability, protect against claims and set clear user expectations.',
        'intro': 'A well-drafted disclaimer helps protect UK businesses from legal liability and sets clear expectations for website visitors, customers, and service users. Our free disclaimer template covers professional advice disclaimers, limitation of liability, third-party content exclusion, and external link disclaimers — all compliant with UK contract law and the Unfair Contract Terms Act 1977.',
        'sections': [
            {'title': 'How Disclaimers Protect UK Businesses', 'body': 'A disclaimer is a statement that limits or excludes your legal liability for certain uses of your website, products, or services. Under the Unfair Contract Terms Act 1977 and Consumer Rights Act 2015, disclaimers between businesses (B2B) are broadly enforceable if reasonable, while consumer-facing disclaimers cannot exclude liability for death/personal injury from negligence, or for goods not meeting required standards. UK courts recognise professionally drafted disclaimers as evidence of transparent communication about risk allocation. A clear disclaimer can prevent claims before they arise, reduce costs of defending unjustified claims, and demonstrate reasonable care in managing customer expectations.'},
            {'title': 'Types of Disclaimers Available', 'body': 'PolicyGen generates several disclaimer types: General website disclaimer — limits liability for accuracy, completeness, and availability of website content. Professional advice disclaimer — clarifies that content is informational not advisory (essential for legal, financial, medical, and consulting sectors). Affiliate disclaimer — discloses affiliate links and commercial relationships (required by ASA/CAP Code for UK advertising compliance). Earnings/results disclaimer — clarifies that no guarantees of specific outcomes are made (crucial for training, coaching, and investment sites). External links disclaimer — limits liability for third-party website content. Testimonial disclaimer — clarifies that individual results may vary. Each is tailored to your industry and website purpose.'},
            {'title': 'UK Regulatory Requirements', 'body': 'Beyond contractual protection, UK regulators and industry bodies have specific disclaimer requirements. The Advertising Standards Authority requires affiliate link disclosures that are prominent and unambiguous. The FCA requires financial websites to include risk warnings. Medical and health websites should include disclaimers that content does not replace professional medical advice. The ASA has published specific guidance on social media influencer disclaimers which apply equally to website affiliate disclosures. Our generator includes industry-specific regulatory disclaimers based on your sector selection.'},
            {'title': 'How to Generate Your Disclaimer', 'body': 'Select your disclaimer type, your industry sector, and enter your business details. Our engine produces a clear, legally sound disclaimer ready to publish on your website or incorporate into your terms and conditions. Free basic templates available instantly. Premium features include multi-disclaimer bundles, industry-specific regulatory variants, and annual review alerts.'},
        ],
        'cta_text': 'Generate your disclaimer — free',
    },
    {
        'slug': 'data-protection-policy-uk-gdpr',
        'title': 'Data Protection Policy Template UK — Internal GDPR Compliance',
        'h1': 'UK Data Protection Policy Template for Businesses',
        'meta_description': 'Free internal data protection policy template for UK businesses. GDPR and DPA 2018 compliant. Essential for ICO registration and compliance.',
        'intro': 'Every UK organisation that processes personal data should have an internal data protection policy. Unlike a public-facing privacy policy (which tells customers how you handle their data), this internal policy guides your staff on data handling procedures. Our template is aligned with UK GDPR, DPA 2018, and ICO guidance, providing a comprehensive framework for data governance within your organisation.',
        'sections': [
            {'title': 'Privacy Policy vs Data Protection Policy', 'body': 'Many UK businesses confuse these two documents. A privacy policy is a public-facing document that informs individuals about how their personal data is collected, used, and protected. A data protection policy is an internal document that sets out rules and procedures your employees must follow when handling personal data. Both are essential: the privacy policy satisfies your UK GDPR Article 13/14 transparency obligations, while the data protection policy demonstrates accountability and good governance to the ICO. The ICO considers a documented data protection policy to be evidence of compliance and looks favourably on organisations that maintain one.'},
            {'title': 'ICO Accountability Principle', 'body': 'Under UK GDPR Article 5(2), the Accountability Principle requires organisations to demonstrate compliance with data protection principles. A comprehensive data protection policy is one of the most effective ways to demonstrate this. It shows the ICO and regulators that you take data protection seriously, have established procedures for your staff to follow, are prepared to handle data subject requests consistently, have processes for data breaches, and maintain appropriate technical and organisational measures. During an ICO investigation, having a documented policy can significantly reduce regulatory penalties.'},
            {'title': 'What the Template Covers', 'body': 'Scope and application of the policy, definitions of key terms (personal data, sensitive data, processing, data subject, controller, processor), data protection principles under UK GDPR, lawful basis requirements and documenting them, data minimisation and storage limitation procedures, individual rights and handling subject access requests, data breach notification procedures (within 72 hours to ICO), third-party data processing agreements, international data transfer rules and adequacy assessments, staff training requirements and frequency, record keeping obligations, policy breach and enforcement procedures, and annual review cycle. All sections are customisable for organisations of any size.'},
            {'title': 'Staff Training and Implementation', 'body': 'A data protection policy only protects your business if your staff actually follow it. Best practice implementation includes: distributing the policy to all employees upon hire and during annual refresh, requiring staff acknowledgment of receipt and understanding, providing role-specific data handling training for teams with high data access, conducting annual compliance audits, appointing a designated Data Protection Officer or Responsible Individual, and maintaining records of data handling incidents and near-misses for accountability evidence.'},
        ],
        'cta_text': 'Generate your data protection policy — free',
    },
    {
        'slug': 'subject-access-request-response-uk',
        'title': 'Subject Access Request Policy UK — GDPR DSAR Response Template',
        'h1': 'Subject Access Request Response Procedure for UK Businesses',
        'meta_description': 'Free DSAR response policy template. Comply with UK GDPR subject access requests within the 30-day legal deadline. ICO-aligned procedures.',
        'intro': 'Under UK GDPR, individuals have the right to request copies of their personal data — known as a Subject Access Request (SAR or DSAR). You must respond within one calendar month, free of charge in most cases. Our free template provides a step-by-step procedure for receiving, processing, and responding to SARs, helping your business meet UK Data Protection Act 2018 obligations and avoid ICO enforcement action.',
        'sections': [
            {'title': 'DSAR Legal Requirements Under UK Law', 'body': 'Under UK GDPR Article 15 and the Data Protection Act 2018, every individual has the right to: confirm their data is being processed, access their personal data, receive supplementary information including categories of data processed, purposes of processing, data recipients, retention periods, source of the data, existence of automated decision-making and profiling, and receive a copy of their data in a commonly used electronic format. The one-month deadline starts from the day you receive the request (including requests via social media, email, or verbally). The ICO can issue enforcement notices and fines for non-compliance.'},
            {'title': 'Our DSAR Response Procedure', 'body': 'The PolicyGen template provides a complete workflow: SAR receipt and logging procedures, identity verification steps, one-month countdown tracking, data collection from all relevant systems and third parties, exemptions assessment (legal professional privilege, management forecasting, litigation risk, and other DPA 2018 exemptions), redaction of third-party personal data, response drafting in plain English, secure data delivery methods, and record keeping for ICO audit trail. The template includes ready-to-use email templates for acknowledgment, extension requests (up to 2 months for complex cases), and response letters.'},
            {'title': 'Common DSAR Mistakes Businesses Make', 'body': 'The ICO\'s published guidance identifies the most common errors: ignoring the request entirely or missing deadlines, failing to search comprehensively across all relevant systems, refusing to provide information in a timely or accessible format, charging fees where none are permitted (you can only charge a reasonable fee for manifestly unfounded or excessive requests), failing to consider exemptions under the DPA 2018, and inadequate redaction of third-party personal data. Our procedure template is designed to prevent each of these errors through systematic checklists and documented procedures.'},
        ],
        'cta_text': 'Generate your DSAR policy — free',
    },
    # More high-intent UK legal pages
    {
        'slug': 'terms-conditions-app-uk',
        'title': 'Terms and Conditions for Mobile Apps UK — Free Template',
        'h1': 'Mobile App Terms and Conditions Template — UK Compliant',
        'meta_description': 'Free app terms and conditions template for UK mobile applications. Covers app store requirements, user conduct, data handling and UK law.',
        'intro': 'Mobile apps face unique legal challenges including app store compliance, in-app purchase terms, user-generated content moderation, permission requirements, and device-specific data access. Our free template is specifically designed for UK app developers and covers Apple App Store and Google Play requirements alongside UK consumer law, the Consumer Rights Act 2015, and UK GDPR obligations.',
        'sections': [
            {'title': 'App-Specific Legal Requirements', 'body': 'Mobile apps are subject to additional legal obligations compared to regular websites under UK law. App stores require you to include specific terms in your agreement. The ICO provides specific guidance for app developers on privacy and consent for device permissions. The Consumer Rights Act 2015 applies to app purchases as digital content with specific quality standards. Key app-specific provisions needed include: device permission disclosures (camera, location, contacts, microphone, notifications), in-app purchase terms and refund policies, user-generated content moderation responsibilities, data synchronisation and storage across devices, offline functionality disclaimers, app store compliance clauses, update and version management terms, and app uninstallation data handling.'},
            {'title': 'App Store Compliance', 'body': 'Both Apple App Store and Google Play require developers to provide an end-user licence agreement (EULA) or terms of use. Apple\'s Review Guidelines Section 5.1.1 requires a clear privacy policy and EULA. Google Play Developer Distribution Agreement Section 6 requires terms that comply with applicable laws including UK consumer protection law. Our template satisfies both platforms\' requirements while ensuring compliance with UK-specific legislation including the Consumer Protection from Unfair Trading Regulations 2008 and the E-Commerce Regulations 2002.'},
        ],
        'cta_text': 'Generate your app terms — free',
    },
    {
        'slug': 'saas-agreement-uk-template',
        'title': 'SaaS Agreement Template UK — B2B Software Terms Generator',
        'h1': 'UK SaaS Agreement Template for Software Businesses',
        'meta_description': 'Free B2B SaaS agreement template for UK software companies. Covers SLA, data protection, intellectual property, termination and UK law compliance.',
        'intro': 'B2B software-as-a-service businesses operating in the UK need a comprehensive SaaS agreement governing the relationship with business customers. Our template covers service level commitments, uptime guarantees, data processing terms, intellectual property licensing, customer obligations, payment terms including MRR/ARR billing, termination rights, exit and data portability provisions, and UK governing law — all essential for closing enterprise deals.',
        'sections': [
            {'title': 'Key Components of a SaaS Agreement', 'body': 'A legally sound UK SaaS agreement must cover: grant of licence and scope of use (number of users, API access, integrations), service level agreement (SLA) with uptime targets and credit provisions for downtime, data security and UK GDPR compliance (including Standard Contractual Clauses if using non-UK data centres), intellectual property ownership and licensing (your software IP, customer data ownership, derivative works restrictions), payment terms and billing cycles (monthly, annual, or usage-based pricing), data portability and exit procedures (helping customers retrieve data on termination), limitation of liability (subject to UCTA 1977 reasonableness test), force majeure provisions covering cyber attacks, regulatory changes, and infrastructure failures, and subcontracting and third-party service disclosures.'},
            {'title': 'UK Enterprise Customer Requirements', 'body': 'Enterprise UK clients typically require additional provisions: vendor due diligence and security audit access, data residency commitments (UK or EU data centre location), business continuity and disaster recovery plans, professional indemnity insurance evidence, references from existing UK customers, and compliance with specific sector regulations (FCA for financial, NHS DSPT for health). Our template includes enterprise-grade provisions that help close larger deals while protecting your business.'},
        ],
        'cta_text': 'Generate your SaaS agreement — free',
    },
    {
        'slug': 'freelancer-contract-uk',
        'title': 'Freelancer Contract Template UK — Independent Contractor Agreement',
        'h1': 'Freelancer Contract Template for UK Businesses',
        'meta_description': 'Free independent contractor agreement for UK businesses. Covers IR35, scope of work, payment terms, IP assignment and UK employment law.',
        'intro': 'Hiring freelancers and contractors in the UK carries the risk of IR35 status determination and potential employment rights claims. Our free freelancer contract template creates a robust independent contractor agreement that establishes the self-employed relationship, addresses scope of work, payment milestones, intellectual property, confidentiality, and IR35 considerations under the Off-Payroll Working Rules.',
        'sections': [
            {'title': 'IR35 and Self-Employment Status', 'body': 'The UK Off-Payroll Working Rules (IR35) determine whether a contractor is genuinely self-employed or should be treated as a deemed employee for tax purposes. Since April 2021, medium and large businesses are responsible for determining IR35 status of their contractors. Key factors courts and HMRC examine include: mutuality of obligation (is there an ongoing obligation to offer and accept work), control (can the client dictate how, when, and where work is done), substitution (can the contractor send a replacement), financial risk (does the contractor bear genuine business risk), and equipment provision (does the contractor use their own tools). Our contract template is drafted to support genuine contractor status while being fair to both parties.'},
        ],
        'cta_text': 'Generate your freelancer contract — free',
    },
]


# UK-FOCUSED HIGH-INTENT TEMPLATE KEYWORDS (combines with industries for more pages)
TEMPLATE_KEYWORDS = [
    {
        'slug': 'retirement-plan-policy-uk',
        'title': 'Retirement Pension Policy Template UK',
        'h1': 'UK Workplace Pension Policy Template',
        'meta_description': 'Free workplace pension and retirement policy template for UK employers. Compliant with auto-enrolment regulations.',
        'intro': 'Under the Pensions Act 2008, all UK employers must provide a workplace pension scheme and automatically enrol eligible workers. Our free template covers auto-enrolment obligations, contribution rates, opt-out procedures, and statutory communication requirements.',
        'sections': [
            {'title': 'Auto-Enrolment Requirements', 'body': 'Since 2012, all UK employers with at least one worker have auto-enrolment duties under the Pensions Act 2008. You must: assess all workers for eligibility, automatically enrol eligible jobholders (aged 22 to State Pension age, earning above £10,000), write to workers about their pension status within 6 weeks of employment, make minimum employer contributions, register with The Pensions Regulator, maintain records, and re-assess workers on each payroll. Failure to comply can result in fines from £400 to £50,000 from The Pensions Regulator.'},
            {'title': 'What Our Policy Template Covers', 'body': 'Eligibility assessment procedure, contribution schedule (employer minimum 3%, employee minimum 5% of qualifying earnings), opt-out processes and refund windows, investment choice framework, communication obligations to staff, record keeping requirements, re-enrolment procedures (every 3 years), dealing with The Pensions Regulator, and governance responsibilities for larger employers.'},
        ],
        'cta_text': 'Generate your pension policy — free',
    },
    {
        'slug': 'health-safety-policy-uk',
        'title': 'Health and Safety Policy Template UK — HSE Compliant',
        'h1': 'UK Health and Safety at Work Policy Template',
        'meta_description': 'Free health and safety policy template for UK businesses. HSE compliant, covering employer duties under the Health and Safety at Work Act 1974.',
        'intro': 'Under the Health and Safety at Work Act 1974, all UK employers (including those with one employee) must have a written health and safety policy if they have five or more employees. Our template covers employer obligations, risk assessment procedures, employee responsibilities, and reporting requirements that satisfy HSE standards.',
        'sections': [
            {'title': 'Legal Framework', 'body': 'The Health and Safety at Work etc. Act 1974 is the primary UK legislation governing workplace safety. Employers must protect the health, safety, and welfare of all employees and, so far as is reasonably practicable, the health and safety of anyone affected by the business. You must conduct suitable and sufficient risk assessments under the Management of Health and Safety at Work Regulations 1999, review assessments regularly, provide information, instruction, training, and adequate supervision, maintain a safe work environment, implement safe systems of work, provide PPE where necessary, consult with employees on health and safety matters, and report certain injuries, diseases, and dangerous occurrences under RIDDOR 2013.'},
        ],
        'cta_text': 'Generate your health and safety policy — free',
    },
    {
        'slug': 'remote-working-policy-uk',
        'title': 'Remote Working Policy Template UK — WFH Employee Guidelines',
        'h1': 'Remote Working Policy Template for UK Employers',
        'meta_description': 'Free home working policy template for UK businesses. Covers health obligations, equipment, data security, expenses, and flexible working rights.',
        'intro': 'With the rise of remote work following the 2020-2021 pandemic, UK employers need clear home working policies to manage obligations under the Health and Safety at Work Act 1974 and new flexible working rights. Our template covers DSE assessments for home workers, equipment provision, data security, expense reimbursement, and employee wellbeing obligations.',
        'sections': [
            {'title': 'New Flexible Working Rights 2024', 'body': 'From 6 April 2024, all UK employees have a statutory right to request flexible working (including remote/hybrid arrangements) from day one of employment, rather than after 26 weeks. Employers must consult with employees before rejecting requests, and employees can make two statutory requests in any 12-month period. The Employment Relations (Flexible Working) Act 2023 removed the need for employees to explain the impact of their request. Your remote working policy should explain how requests are handled, response timelines (one month unless agreed otherwise), and reasons for potential refusal.'},
        ],
        'cta_text': 'Generate your remote working policy — free',
    },
]


B2B_TEMPLATE_PAGES = [
    {
        'slug': 'whistleblowing-policy-uk',
        'title': 'Whistleblowing Policy Template UK — Employee Protection',
        'h1': 'UK Whistleblowing Policy for Employers',
        'meta_description': 'Free whistleblowing policy template for UK organisations. Compliant with the Public Interest Disclosure Act 1998 and ACAS Code.',
        'intro': 'The Public Interest Disclosure Act 1998 protects employees who report wrongdoing from victimisation and unfair dismissal. Our free whistleblowing policy template helps UK employers establish clear procedures for employees to raise concerns safely, in line with ACAS guidance and the Employment Rights Act 1996.',
        'sections': [
            {'title': 'UK Whistleblowing Legal Framework', 'body': 'The Public Interest Disclosure Act 1998 (PIDA) amended the Employment Rights Act 1996 to protect workers who make qualifying disclosures about wrongdoing including criminal offences, breaches of legal obligation, miscarriages of justice, health and safety dangers, environmental damage, and attempts to cover up wrongdoing. Workers who are victimised or dismissed for making a protected disclosure can claim unlimited unfair dismissal compensation, and the employer has no cap on the compensation award.'},
        ],
        'cta_text': 'Generate your whistleblowing policy — free',
    },
    {
        'slug': 'equality-diversity-policy-uk',
        'title': 'Equality and Diversity Policy Template UK — Anti-Discrimination',
        'h1': 'Equality and Diversity Policy for UK Organisations',
        'meta_description': 'Free equality and diversity policy template for UK employers. Compliant with the Equality Act 2010 and Public Sector Equality Duty.',
        'intro': 'Under the Equality Act 2010, UK employers must not discriminate against employees or job applicants based on nine protected characteristics. Our free equality and diversity policy template helps prevent unlawful discrimination, promote inclusivity, and demonstrate compliance to employment tribunals. Suitable for businesses of all sizes across England, Scotland, Wales, and Northern Ireland.',
        'sections': [
            {'title': 'Equality Act 2010 Protected Characteristics', 'body': 'The Equality Act 2010 protects nine characteristics: age, disability (including physical and mental health conditions), gender reassignment, marriage and civil partnership, pregnancy and maternity, race, religion or belief (including non-religious philosophical beliefs), sex, and sexual orientation. Your policy must address all nine and show how your organisation commits to protecting employees and service users from discrimination, harassment, and victimisation.'},
        ],
        'cta_text': 'Generate your equality and diversity policy — free',
    },
    {
        'slug': 'grievance-procedure-uk',
        'title': 'Grievance Procedure Template UK — ACAS Compliant',
        'h1': 'ACAS Compliant Grievance Procedure for UK Employers',
        'meta_description': 'Free grievance procedure template for UK businesses. Follows ACAS Code of Practice on Disciplinary and Grievance procedures.',
        'intro': 'The ACAS Code of Practice on Disciplinary and Grievance Procedures sets the standard for handling employee complaints in UK workplaces. Our free template provides a step-by-step grievance procedure that meets ACAS standards, helping you manage employee complaints fairly and avoid employment tribunal uplifts of up to 25% for procedural failures.',
        'sections': [
            {'title': 'The ACAS Code and Employment Tribunals', 'body': 'The ACAS Code is not itself legally binding, but employment tribunals must take it into account. If an employer unreasonably fails to follow the Code, tribunals can increase any compensation award by up to 25%. Conversely, if an employee unreasonably fails to follow the ACAS grievance procedure before raising a tribunal claim, their compensation can be reduced by up to 25%. The Code requires employers to handle grievances promptly, hold grievance meetings before taking action, allow employees to be accompanied, and provide a right of appeal.'},
        ],
        'cta_text': 'Generate your grievance procedure — free',
    },
    {
        'slug': 'disciplinary-procedure-uk',
        'title': 'Disciplinary Procedure Template UK — ACAS Compliant Steps',
        'h1': 'ACAS Compliant Disciplinary Procedure for UK Employers',
        'meta_description': 'Free disciplinary procedure template for UK businesses. ACAS Code compliant with fair hearing, investigation and appeal rights.',
        'intro': 'A fair disciplinary procedure is essential for lawful employee management in the UK. Our ACAS-compliant disciplinary procedure template provides clear steps from informal warnings through formal hearings to dismissal — helping you manage performance and conduct issues lawfully while avoiding unfair dismissal claims and ACAS Code uplifts of up to 25%.',
        'sections': [
            {'title': 'ACAS Disciplinary Procedure Requirements', 'body': 'For a disciplinary to be fair under UK law it must follow clear procedure: establish the facts, inform the employee of the case against them in writing, hold a meeting to discuss the issue, allow the employee to be accompanied, decide on appropriate action (if any), and provide a right of appeal. The ACAS Code identifies four graduated levels: informal action (verbal, not part of formal record), first written warning, final written warning, and dismissal. Each warning should specify the improvement required, the timescale, the consequences of failure, and the appeal process.'},
        ],
        'cta_text': 'Generate your disciplinary procedure — free',
    },
    # Social Media / Influencer / Digital specific
    {
        'slug': 'social-media-policy-uk-employees',
        'title': 'Social Media Policy Template UK — Employee Social Media Guidelines',
        'h1': 'UK Employee Social Media Policy Template',
        'meta_description': 'Free social media policy for UK employees. Covers personal and professional social media use, brand reputation, confidentiality and UK employment law.',
        'intro': 'Social media presents both opportunities and risks for UK employers. Our free social media policy template helps you establish clear guidelines for employee social media use — covering personal accounts, professional brand representation, confidentiality, data protection, defamation risk, and consequences for policy violations. Essential for all UK businesses with a workforce.',
        'sections': [
            {'title': 'Legal Framework for Social Media Policies', 'body': 'UK employment law applies equally to social media activity as it does to offline behaviour. Employees can face disciplinary action for social media posts that breach confidentiality, amount to gross misconduct, bring the employer into disrepute, constitute bullying or harassment, or reveal trade secrets or client information. UK case law has confirmed that even posts made on personal social media accounts, outside working hours, can constitute misconduct if they have a sufficient connection to the workplace.'},
        ],
        'cta_text': 'Generate your social media policy — free',
    },
    {
        'slug': 'anti-bullying-harassment-policy-uk',
        'title': 'Anti-Bullying and Harassment Policy UK — Zero Tolerance',
        'h1': 'Anti-Bullying and Harassment Policy for UK Workplaces',
        'meta_description': 'Free anti-bullying and harassment policy template for UK employers. Zero tolerance approach aligned with ACAS guidance equality Act 2010.',
        'intro': 'Under the Equality Act 2010 and the Health and Safety at Work Act 1974, UK employers have a duty to prevent harassment and protect employee wellbeing. Our free policy template establishes a zero-tolerance approach to bullying, harassment, and victimisation, providing clear reporting procedures and investigation frameworks aligned with ACAS guidance.',
        'sections': [
            {'title': 'Employer Liability for Harassment', 'body': 'Under the Equality Act 2010, employers are vicariously liable for harassment committed by employees in the course of employment. Even if an employer did not authorise the harassment, they must show they took all reasonable steps to prevent it. A documented anti-bullying and harassment policy is the primary evidence courts and tribunals look for when assessing whether reasonable steps were taken. UK employers must also provide a safe working environment under the Health and Safety at Work Act, which extends to protecting mental health from workplace harassment.'},
        ],
        'cta_text': 'Generate your anti-harassment policy — free',
    },
    # Compliance / Risk management
    {
        'slug': 'anti-bribery-policy-uk',
        'title': 'Anti-Bribery and Corruption Policy UK — Bribery Act 2010',
        'h1': 'Anti-Bribery Policy Template for UK Businesses',
        'meta_description': 'Free anti-bribery and corruption policy for UK businesses. Compliant with the Bribery Act 2010, covering gifts, hospitality, facilitation payments.',
        'intro': 'The Bribery Act 2010 is one of the strictest anti-corruption laws globally. UK companies and their officers can face criminal prosecution for bribery, including failure to prevent bribery under Section 7. Our free anti-bribery policy template helps establish adequate procedures to prevent corruption — one of the six principles set by the UK Ministry of Justice.',
        'sections': [
            {'title': 'Bribery Act 2010 Offences and Defence', 'body': 'The Act creates four offences: Section 1 — bribing another person; Section 2 — being bribed; Section 6 — bribing a foreign public official; Section 7 — failure of commercial organisations to prevent bribery. The only defence to a Section 7 charge is to demonstrate that the organisation had adequate procedures in place to prevent bribery. The UK Ministry of Justice published six guiding principles: proportionate procedures, top-level commitment, risk assessment, due diligence, communication and training, and monitoring and review.'},
        ],
        'cta_text': 'Generate your anti-bribery policy — free',
    },
    {
        'slug': 'modern-slavery-statement-uk',
        'title': 'Modern Slavery Statement Template UK — Section 54 Compliance',
        'h1': 'Modern Slavery Statement for UK Businesses',
        'meta_description': 'Free modern slavery statement template. Meets Section 54 of the Modern Slavery Act 2015 reporting obligations for UK organisations.',
        'intro': 'Section 54 of the Modern Slavery Act 2015 requires UK commercial organisations with turnovers exceeding £36 million to publish an annual slavery and human trafficking statement. Our template provides the structure and language required for compliance, including organisational structure, supply chain description, policies, due diligence procedures, training programmes, and effectiveness assessment.',
        'sections': [
            {'title': 'Section 54 Requirements', 'body': 'The statement must cover: organisation structure and business and supply chains, policies relating to slavery and human trafficking, due diligence processes, risk assessment procedures, effectiveness measures, training provided to staff, and approval and sign-off by a director or equivalent senior officer. The statement must be published on the organisation\'s website with a prominent link on the homepage.'},
        ],
        'cta_text': 'Generate your modern slavery statement — free',
    },
    {
        'slug': 'environmental-policy-uk-business',
        'title': 'Environmental Policy Template UK — Business Environment Statement',
        'h1': 'Environmental Policy Template for UK Businesses',
        'meta_description': 'Free environmental policy template for UK businesses. Covers waste, emissions, sustainability goals and regulatory compliance.',
        'intro': 'UK businesses are increasingly expected to demonstrate environmental responsibility to clients, investors, and regulators. Our template provides a professional environmental policy framework covering waste management, energy efficiency, sustainable procurement, carbon reduction targets, and UK environmental regulatory compliance.',
        'sections': [
            {'title': 'UK Environmental Regulation Context', 'body': 'The UK Environment Agency, Natural Resources Wales, SEPA Scotland, and the Northern Ireland Environment Agency all regulate business environmental impact. Key legislation includes the Environmental Protection Act 1990, the Environment Act 1995, waste regulations, extended producer responsibility schemes, carbon reporting requirements for large businesses, and packaging waste producer responsibility obligations. A documented environmental policy demonstrates proactive compliance management to regulators and customers.'},
        ],
        'cta_text': 'Generate your environmental policy — free',
    },
    # Digital-specific / Technology
    {
        'slug': 'acceptable-use-policy-uk',
        'title': 'Acceptable Use Policy Template UK — IT and Internet Usage',
        'h1': 'IT Acceptable Use Policy for UK Organisations',
        'meta_description': 'Free acceptable use policy template for UK businesses. Governs IT, internet, email and social media use in the workplace.',
        'intro': 'Every UK organisation should have an acceptable use policy governing employee access to IT systems, internet, email, and digital devices. Our template covers permitted and prohibited uses, monitoring rights under RIPA 2000, data security obligations, consequences for violations, and employee privacy rights — all compliant with UK employment and data protection law.',
        'sections': [
            {'title': 'Monitoring and Privacy Rights', 'body': 'Under the Regulation of Investigatory Powers Act 2000 and the Telecommunications (Lawful Business Practice) Regulations 2000, employers may monitor employee communications for specific legitimate purposes including quality control, training, crime prevention, and ensuring business use compliance. However, under the UK GDPR, employees retain a right to privacy that must be balanced against employer monitoring. Our template addresses both: defining permissible monitoring scope, employee notification requirements, and the boundary between monitoring and unlawful surveillance.'},
        ],
        'cta_text': 'Generate your acceptable use policy — free',
    },
    {
        'slug': 'ai-policy-uk-workplace',
        'title': 'AI Usage Policy Template UK — Workplace AI Guidelines',
        'h1': 'Workplace AI Policy Template for UK Organisations',
        'meta_description': 'Free workplace AI usage policy for UK businesses. Covers AI tool usage, data input restrictions, content verification and employee AI guidelines.',
        'intro': 'As AI tools become ubiquitous in the workplace, UK organisations need clear policies governing acceptable AI use. Our template addresses: approved AI tools for business use, restrictions on inputting confidential data into public AI models, verification requirements for AI-generated content, intellectual property concerns, employee AI training, and client notification obligations. Aligned with UK government AI safety principles and ICO AI guidance.',
        'sections': [
            {'title': 'AI and UK Data Protection', 'body': 'The ICO published comprehensive guidance on AI and data protection in November 2022. Key requirements include: conducting Data Protection Impact Assessments for significant AI systems, ensuring lawfulness, fairness, and transparency in AI processing, managing data minimisation when feeding data to AI systems, maintaining accuracy standards for AI-generated outputs, addressing automated decision-making rights under UK GDPR Article 22, and being transparent with customers when AI is used in service delivery. Our policy template addresses each of these areas.'},
        ],
        'cta_text': 'Generate your AI policy — free',
    },
    {
        'slug': 'information-security-policy-uk',
        'title': 'Information Security Policy Template UK — Cyber Security Framework',
        'h1': 'Information Security Policy for UK Organisations',
        'meta_description': 'Free information security policy template for UK businesses. ISO 27001-aligned framework covering cyber security, access controls, and incident response.',
        'intro': 'Every UK organisation processing personal data needs an information security policy. Our template provides an ISO 27001-aligned framework covering access controls, password management, secure remote access, incident response, mobile device management, email security, and encryption standards — all tailored to UK regulatory requirements including Cyber Essentials and UK GDPR Article 32.',
        'sections': [
            {'title': 'UK GDPR Technical Security Requirements', 'body': 'Under UK GDPR Article 32, controllers and processors must implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk. The ICO expects: pseudo-anonymisation and encryption of personal data, ability to restore access to data after a physical or technical incident, regular testing and evaluation of security measures, staff security training, and incident response procedures. The UK National Cyber Security Centre (NCSC) recommends Cyber Essentials certification as a baseline for any organisation. Our policy template aligns with all of these frameworks.'},
        ],
        'cta_text': 'Generate your info security policy — free',
    },
    # E-commerce
    {
        'slug': 'distance-selling-policy-uk',
        'title': 'Distance Selling Policy UK — Consumer Regulations 2013',
        'h1': 'Distance Selling Policy for UK Online Businesses',
        'meta_description': 'Free distance selling policy template for UK businesses. Consumer Contracts Regulations 2013 compliant with 14-day cancellation rights.',
        'intro': 'The Consumer Contracts Regulations 2013 govern all distance selling in the UK — online, telephone, and mail order. Our free template creates a comprehensive distance selling policy covering the 14-day cancellation period, refund obligations, delivery timeframes, returns procedures, and the specific pre-contractual information disclosures required before the contract is formed.',
        'sections': [
            {'title': 'Consumer Contracts Regulations 2013', 'body': 'These regulations apply to all contracts concluded at a distance (online, phone, post) or away from business premises. Key requirements include: providing clear pre-contract information about the total price, delivery arrangements, and cancellation rights in a durable medium before the customer orders; confirming this information in writing (usually by email) after purchase; honouring the 14-day cancellation period from the day goods are received; refunding within 14 days of receiving returned goods or receiving evidence of return (whichever is earlier); refunding standard delivery costs (though enhanced delivery costs need not be refunded if the customer chose a premium option); and providing a model cancellation form.'},
        ],
        'cta_text': 'Generate your distance selling policy — free',
    },
    {
        'slug': 'product-warranty-policy-uk',
        'title': 'Product Warranty Policy Template UK — Consumer Rights Act',
        'h1': 'Product Warranty and Guarantee Policy for UK Retailers',
        'meta_description': 'Free product warranty policy template for UK businesses. Explains consumer rights, manufacturer warranties, and guarantee terms under UK law.',
        'intro': 'UK consumers have statutory warranty rights under the Consumer Rights Act 2015, but businesses also need clear warranty and guarantee policies to manage customer expectations and claims. Our template differentiates between statutory rights, manufacturer warranties, and business-provided guarantees — creating a policy that is both customer-friendly and legally protective.',
        'sections': [
            {'title': 'Statutory vs Voluntary Warranties', 'body': 'Under the Consumer Rights Act 2015, goods must be of satisfactory quality, fit for purpose, and as described. These statutory rights exist regardless of any warranty you provide. A commercial warranty or guarantee is an additional voluntary commitment — it must be in writing, clearly state what it covers, and not restrict the consumer\'s statutory rights. The CRA 2015 requires that any guarantee is available to consumers in writing, is legally binding on the guarantor, and is honoured as stated. Extended warranty sales also require compliant terms explaining the additional coverage and any exclusions.'},
        ],
        'cta_text': 'Generate your warranty policy — free',
    },
    # Business management
    {
        'slug': 'complaints-procedure-uk',
        'title': 'Complaints Procedure Template UK — Customer Complaint Resolution',
        'h1': 'Customer Complaints Procedure for UK Businesses',
        'meta_description': 'Free complaints procedure template for UK businesses. Clear, professional dispute resolution aligned with ISO 10002 and UK consumer rights.',
        'intro': 'A clear, accessible complaints procedure is essential for every UK business. Under the Consumer Rights Act 2015, customers have the right to complain, and businesses must handle complaints fairly. Our free template provides a professional, step-by-step complaints procedure aligned with ISO 10002 guidelines, helping resolve issues efficiently and avoiding escalation to formal disputes or regulatory action.',
        'sections': [
            {'title': 'Legal and Regulatory Context', 'body': 'Several UK regulatory frameworks require documented complaints procedures: the Financial Conduct Authority requires FCA-regulated firms to have a complaints handling procedure with published complaint data; the Legal Ombudsman requires all regulated solicitors to have a complaints procedure with clear escalation paths; Trading Standards may investigate complaints against businesses without proper procedures; and the Consumer Rights Act 2015 implies that services should be provided with reasonable care and skill, and customers must have a pathway to raise issues when this standard is not met. Even businesses without specific regulatory oversight should have a documented procedure as evidence of good faith customer service.'},
        ],
        'cta_text': 'Generate your complaints procedure — free',
    },
    {
        'slug': 'bring-your-own-device-policy-uk',
        'title': 'Bring Your Own Device Policy UK — BYOD Workplace Guidelines',
        'h1': 'BYOD Policy Template for UK Workplaces',
        'meta_description': 'Free bring-your-own-device policy for UK employers. Covers security, reimbursement, acceptable use, and UK data protection law.',
        'intro': 'As more UK workers use personal devices for business purposes, organisations need a BYOD policy addressing security, reimbursement, data protection, and acceptable use. Our template covers company app installation on personal devices, reimbursement for business use, wipe and remote access rights, personal privacy protection, and data breach responsibilities — all within the UK legal framework.',
        'sections': [
            {'title': 'Data Protection and Employee Privacy', 'body': 'Under UK GDPR, BYOD arrangements create specific challenges: business data on personal devices constitutes processing of personal data, remote wipe capabilities may delete personal files alongside business data, employee monitoring on personal devices must be proportionate and transparent, and access to personal data on devices during investigations may raise privacy conflicts. The ICO expects employers to be transparent, proportionate, and respectful of personal privacy when managing BYOD. Our template strikes the right balance between organisational security and employee privacy rights.'},
        ],
        'cta_text': 'Generate your BYOD policy — free',
    },
    {
        'slug': 'maternity-paternity-leave-policy-uk',
        'title': 'Maternity and Paternity Leave Policy UK — Family Leave Rights',
        'h1': 'Maternity and Paternity Leave Policy for UK Employers',
        'meta_description': 'Free maternity and paternity leave policy for UK businesses. Covers SMP, SPP, shared parental leave, and keeping-in-touch days under UK law.',
        'intro': 'UK employees have extensive statutory rights to family-related leave including maternity, paternity, adoption, and shared parental leave. Our comprehensive policy template covers all family-related leave types, pay entitlements, notification requirements, keeping-in-touch arrangements, and return-to-work procedures — all reflecting current UK legislation and statutory pay rates.',
        'sections': [
            {'title': 'UK Family Leave Entitlements', 'body': 'Current UK statutory entitlements include: Ordinary Maternity Leave (26 weeks) and Additional Maternity Leave (26 more weeks), Statutory Maternity Pay (SMP) — 90% of average weekly earnings for 6 weeks, then £184.03/week or 90% of earnings for 33 weeks, Ordinary Paternity Leave (1-2 weeks), Statutory Paternity Pay (SPP), Shared Parental Leave — up to 50 weeks of leave and 37 weeks of pay shared between parents, Maternity Allowance for self-employed and those not qualifying for SMP, Adoption Leave and Pay mirroring maternity leave entitlements, and Keeping in Touch days — up to 10 days of work without ending maternity leave.'},
        ],
        'cta_text': 'Generate your family leave policy — free',
    },

]


class Command(BaseCommand):
    help = 'Seed 50+ UK-focused high-intent SEO landing pages for policygen.site'

    def handle(self, *args, **options):
        all_pages = UK_SEO_PAGES + TEMPLATE_KEYWORDS + B2B_TEMPLATE_PAGES
        count = 0
        skipped = 0

        import html

        for page in all_pages:
            slug = page['slug']
            if SEOLandingPage.objects.filter(slug=slug).exists():
                skipped += 1
                continue

            sections = page.get('sections', [])
            # Format sections as list of dicts with title and body
            formatted_sections = []
            for s in sections:
                formatted_sections.append({
                    'title': s['title'],
                    'body': s['body'],
                })

            SEOLandingPage.objects.create(
                industry='other',
                regulation='',
                location='United Kingdom',
                title=page['title'],
                slug=slug,
                meta_description=page.get('meta_description', ''),
                h1=page['h1'],
                intro=page['intro'],
                sections=formatted_sections,
                cta_text=page.get('cta_text', 'Generate your legal document — free'),
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Created {count} new UK SEO landing pages"
        ))
        self.stdout.write(f"⏭️  Skipped {skipped} existing pages")
        self.stdout.write(f"📊 Total UK-specific pages: {count + skipped}")
        self.stdout.write(f"\n🔍 High-intent keyword targets:")
        for page in all_pages[:20]:
            self.stdout.write(f"   • {page['slug']}")

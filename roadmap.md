# Project Roadmap: PolicyGen Frontend Redesign

## Goals
- [x] Complete vintage print shop retro redesign
- [x] All 19 templates updated
- [x] Responsive at all breakpoints
- [x] No broken functionality
- [x] SEO audit — all critical & high issues fixed

## Resume Checkpoint
- Last updated: 2026-04-28 07:50
- Last completed task: T1 — Fix hardcoded counter (TDD: RED→GREEN, 5/5 passing)
- Next task: T2 — Email capture on free tier
- Sprint: 4 — BUSINESS GROWTH
- Status: IN PROGRESS

## Phase 1: Vercel-Inspired Redesign — Sprint 1 ✅ (superseded)

## Phase 2: Vintage Print Shop — Sprint 2 ✅

### Design System: Vintage Print Shop
- Fonts: Playfair Display (headings), Lora (body), Courier Prime (mono)
- Palette: Cream paper (#f5f0e1), dark ink (#2c1810), deep red (#8b2500), gold (#b8860b)
- Technique: Paper texture CSS background, double borders, letterpress buttons, stacked paper cards
- Feel: 1920s law office meets modern web

### Tasks
- [x] Rewrite style.css (complete retro design system) — 905 lines
- [x] Update base.html (Playfair/Lora/Courier fonts, gold-on-ink header)
- [x] Restyle home.html (letterpress buttons, stacked paper cards, vintage table)
- [x] Update register.html
- [x] Update login.html
- [x] Update pricing.html
- [x] Update generator_step1/2/3.html
- [x] Update score_checker.html
- [x] Update compare.html
- [x] Update seo_landing.html
- [x] Update legal_cookies/privacy/terms.html
- [x] Update document_view.html
- [x] Verify all 19 templates compile
- [x] Ready to push to GitHub

## Phase 3: SEO Audit & Fixes — Sprint 3 ✅

### SEO Audit Findings (2026-04-26)

#### 🔴 Critical Issues — ALL FIXED
- [x] **C1 — No meta description support in base.html:** Added `{% block meta_description %}` to base.html + descriptions on all 19 templates.
- [x] **C2 — No canonical URL tag:** Added `{% block canonical_url %}` to base.html (self-referencing by default).
- [x] **C3 — No robots.txt:** Created `/static/robots.txt` + view at `/robots.txt` URL.
- [x] **C4 — No XML sitemap:** Created `policies/sitemaps.py` with static + SEO landing page sitemaps, wired at `/sitemap.xml` with 1-hour cache.
- [x] **C5 — SEO landing pages ignore stored meta_description:** Now renders `page.meta_description` in meta tags + OG + Twitter cards.

#### 🟠 High-Priority Issues — ALL FIXED
- [x] **H1 — No Open Graph / Twitter Card tags:** Added `og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `twitter:card` (summary_large_image), `twitter:title`, `twitter:description`, `twitter:image` blocks to base.html.
- [x] **H2 — No structured data / JSON-LD schema:** Added SoftwareApplication JSON-LD to base.html (homepage), Article schema to blog template.
- [x] **H3 — Blog app not wired into URLs:** Added `blog` to INSTALLED_APPS, added `include('blog.urls')` to config/urls.py.
- [x] **H4 — No favicon:** Added SVG favicon + apple-touch-icon + default OG image.

#### 🟡 Medium-Priority Issues — ALL FIXED
- [x] **M1 — No hreflang tags:** Added `hreflang="en"` and `hreflang="x-default"` to base.html.
- [x] **M2 — Blog template uses old design:** Rewrote `employment-contract-template-uk-2026.html` to retro print shop design, fixed domain to policygen.site.
- [x] **M3 — 404/500 error pages use old design:** Rewrote both with retro style (Playfair Display, cream paper, ink borders, letterpress buttons).

### Files Changed (Sprint 3)
- `templates/base.html` — Major rewrite: +meta description, canonical, OG, Twitter, hreflang, JSON-LD, favicon
- `config/settings.py` — Added `django.contrib.sitemaps` + `blog` to INSTALLED_APPS
- `config/urls.py` — Added robots.txt view, sitemap.xml, blog URLs
- `policies/sitemaps.py` — NEW: StaticSitemap + SEOSitemap
- `static/robots.txt` — NEW
- `static/img/favicon.svg` — NEW
- `static/img/apple-touch-icon.svg` — NEW
- `static/img/og-default.svg` — NEW
- `templates/policies/pricing.html` — +meta_description + OG + Twitter
- `templates/policies/score_checker.html` — +meta_description + OG + Twitter
- `templates/policies/compare.html` — +meta_description + OG + Twitter
- `templates/policies/generator_step1.html` — +meta_description
- `templates/policies/generator_step2.html` — +meta_description
- `templates/policies/generator_step3.html` — +meta_description
- `templates/policies/seo_landing.html` — +meta_description + OG + Twitter from model
- `templates/policies/legal_privacy.html` — +meta_description
- `templates/policies/legal_terms.html` — +meta_description
- `templates/policies/legal_cookies.html` — +meta_description
- `templates/policies/document_list.html` — +meta_description
- `templates/policies/document_view.html` — +meta_description
- `templates/users/login.html` — +meta_description
- `templates/users/register.html` — +meta_description + OG + Twitter
- `templates/404.html` — Retro print shop redesign
- `templates/500.html` — Retro print shop redesign
- `templates/blog/employment-contract-template-uk-2026.html` — Retro redesign + Article schema + fixed domain

## Phase 5: Live Site Audit — 2026-04-29 🔴

**Overall Score: 6.2/10**

| # | Dimension | Score | Finding | Improvement Needed |
|---|-----------|-------|---------|-------------------|
| 1 | Images & Visuals | 3/10 | **Zero real images** — all visuals are emoji/unicode. No product screenshots, no logo image, no hero graphic. | Add real logo image, 1-2 product screenshots/hero illustration, and author photos for testimonials. Target 5-8 meaningful images with alt text. |
| 2 | Layout & Structure | 7/10 | Clean single-column layout with good whitespace. H3 appears directly after H1 — semantic heading order broken (H1→H3 with no H2). | Fix heading hierarchy: insert H2 between H1 and first H3, or promote H3 to H2 per WCAG 1.3.1. (5 min) |
| 3 | Typography | 8/10 | Playfair Display + Lora + Courier Prime — excellent law-firm serif pairing. 1.7 line-height for readability. Good contrast (#2c1810 on #f5f0e1). Google Fonts with preconnect + display=swap. | Set min-font-size of 16px on mobile inputs to prevent iOS zoom. Use Courier Prime more intentionally for data points/quotes. (10 min) |
| 4 | Mobile Responsive | 6/10 | Viewport meta ✓. CSS media queries detected. Mobile CTA bar present. 8 touch targets below 44px (WCAG 2.5.5). No hamburger menu. Footer links dense on small screens. | Enforce 44×44px minimum touch targets. Add hamburger menu at ≤768px. Test at 375px (iPhone SE) and 768px (iPad). (2-3 hrs) |
| 5 | UX & CTAs | 8/10 | Strong primary CTA ("Generate My Free Policy") at 3× strategic scroll points. All 19 links have valid, distinct hrefs — zero empty/hash links. Missing contact form on site. | Add /contact/ form for users without email clients. Add FAQ link in footer. (1-2 hrs) |
| 6 | Console Errors | 10/10 | Zero JS errors, zero console messages, zero failed API calls. Site is fully static/server-rendered with no client-side JS. | No fixes needed. When JS is added, maintain this standard with error boundaries. |
| 7 | Content Quality | 6/10 | Copywriting is sharp and persuasive ("lawyers charge £500+", "90 seconds"). Legal pages have substantive content. **Testimonials appear fabricated** (initials-only: SR/MK/JL, no photos). "94% of websites have outdated policies" unsourced. "Freelance" typo. | Replace fabricated testimonials with real ones (full names, photos, companies). Cite sources for stats. Fix "Freelance" → "Freelance". Make doc counter dynamic if meant to appear live. (2-4 hrs) |
| 8 | SEO Basics | 3/10 | Title ✓, H1 ✓, viewport ✓, lang="en" ✓. **Missing**: meta description, all OG tags, Twitter card, canonical URL, favicon, zero JSON-LD structured data. Critical gaps for search visibility and social sharing. | Add meta description (150-160 chars). Add full OG + Twitter card tags. Add canonical. Add favicon + apple-touch-icon. Add Organization JSON-LD. Test with Google Rich Results + Facebook Sharing Debugger. (1-2 hrs) |
| 9 | Trust Signals | 5/10 | Real privacy/TOS/cookie pages with substantive content. Stripe mentioned for payments. **Testimonials appear fabricated** (initials-only, no photos, generic quotes). No business address or phone. Only contact: mailto:hello@policygen.site. | Replace fake testimonials. Add physical business address + phone (required for legal services trust). Add Trustpilot/Google Reviews widget. Add SSL security badge. (3-5 hrs) |
| 10 | Overall Feel | 6/10 | Strong first impression — law-firm aesthetic with serif typography, cream palette, confident copy. Undermined by emoji-only visuals, fake-looking testimonials, missing SEO fundamentals, sparse contact details. Would NOT trust with credit card without independent verification. | Address TOP3 below. Once visuals, trust, and SEO are strengthened, the design and content quality will carry a much more credible impression. (6-12 hrs total) |

### 🔴 TOP 3 PRIORITY FIXES (from audit)
1. **Add real images and favicon** — Emoji-only visuals undermine credibility for a legal document service. No favicon makes the site look incomplete. → Add professional logo image, 1-2 product screenshots, testimonial author photos. Add favicon.ico (32×32), favicon-32x32.png, apple-touch-icon. All images need alt text. (2-3 hrs)
2. **Fix all SEO fundamentals (meta description, OG tags, structured data, canonical)** — Zero social sharing preview. No structured data = no rich results. Missing meta description = Google auto-generates snippets. → Add `<meta name="description">`, full og:tags, twitter:card, canonical `<link>`, Organization JSON-LD. Test with Google Rich Results + Facebook Debugger. (1-2 hrs)
3. **Replace fabricated testimonials with real ones + add business contact details** — Initials-only names (SR, MK, JL) with no photos are an immediate red flag. No address/phone for a legal service is a trust killer. → Collect 3 real testimonials with full names, headshots, role, company. Add business address + phone to footer and /contact. If not possible, remove fake testimonials — none is better than fabricated. (3-5 hrs)

### Issues
- None

### Security
- None

---

## Phase 4.5: Live Site Audit — 2026-04-28 🔴

**Overall Score: 6.2/10**

| # | Dimension | Score | Finding | Improvement Needed |
|---|-----------|-------|---------|-------------------|
| 1 | Images & Visuals | 4/10 | **Zero `<img>` tags site-wide.** Only 1 inline SVG + emoji-based icons. No hero image, product screenshots, or visual demos. Testimonials use initials instead of photos. Trust badges = emoji-only. | Add hero/product screenshot above fold. Add 1 illustration per "How it works" step. Replace emoji badges with actual graphics (GDPR, Stripe, SSL). |
| 2 | Layout & Structure | 7/10 | Clean single-column flow with strong comparison table. No layout breaks. Entirely text-heavy — zero visual dividers or imagery. | Add subtle section dividers or alternating background tints. Consider 2-col grid for document-type cards. |
| 3 | Typography | 6/10 | Good font stack (Playfair Display, Lora, Courier Prime) fits legal brand. **Heading hierarchy broken:** H1→H3 skip with no H2. Pricing page has **no H1 at all**. "Freelance" misspelled in testimonial. | Fix H1→H2→H3 flow on all pages. Add `<h1>` to /pricing/. Fix "Freelance" typo. |
| 4 | Mobile Responsive | 7/10 | Viewport meta present. Single-column adapts naturally. **No hamburger menu** — nav links stay inline and will crowd on phones. No mobile-specific tap-target sizing. | Add hamburger menu at ≤768px. Ensure CTA buttons ≥44px tap targets. Test on real devices. |
| 5 | UX & CTAs | 7/10 | Strong action-oriented CTAs at top/middle/bottom. Free tier prominently advertised. Primary and secondary CTAs visually identical. "Contact us" is bare `mailto:` with no form. | Style primary CTAs distinctly (filled vs outlined). Add contact form. Add sticky CTA on mobile. |
| 6 | Console Errors | 9/10 | **Zero JS errors, zero warnings** across all 4 pages tested. Cleanest codebase of all sites. | Add Web Vitals monitoring (web-vitals.js or RUM) for real-user data. |
| 7 | Content Quality | 8/10 | Strong benefit-driven copy. Clear value prop ("90 seconds vs £500 lawyer"). Excellent comparison table. Real testimonials with specific claims. Legal pages thorough and complete. "Freelance" typo noted. | Fix typo. Add 1-2 case studies or "before/after" examples. |
| 8 | SEO Basics | 2/10 | **CRITICAL: No meta description, no OG tags, no canonical URLs, no structured data (JSON-LD), no favicon, no robots meta, no sitemap detected.** Pages invisible to Google and share poorly on social. Page titles decent. NOTE: These fixes exist in local roadmap (Phase 3) but appear NOT DEPLOYED to live site. | Deploy Phase 3 SEO fixes to production: add meta descriptions, OG tags, canonical URLs, JSON-LD schema, favicon, robots.txt, sitemap.xml. **Highest-ROI fix.** |
| 9 | Trust Signals | 6/10 | Strong social proof (2,000+ businesses, 3,847 docs/mo, 3 testimonials with ★★★★★). Money-back guarantee. Legal pages exist. **Missing:** no customer photos, no Stripe/SSL trust badges, no media mentions, no client logos. Testimonials text-only with initials. | Add Stripe + SSL trust badges. Add client logos if any recognizable clients exist. |
| 10 | Overall Feel | 6/10 | Solid product, clean code (zero JS errors), thorough legal pages, persuasive copy. Crippled by missing SEO fundamentals (won't rank), zero imagery (feels untrustworthy), and heading hierarchy issues. Few hours of SEO + visual polish → dramatic improvement. | Deploy Phase 3 SEO fixes immediately. Add hero image. Fix headings. |

### 🔴 TOP 3 PRIORITY FIXES (from audit)
1. **Deploy Phase 3 SEO fixes to production** — Meta descriptions, OG tags, canonical URLs, JSON-LD, favicon, robots.txt, sitemap all exist in codebase but NOT on live site. The site is invisible to Google. Estimated: 1 hr to deploy.
2. **Add visual assets (hero image, product screenshot, trust badges)** — Text-only legal site looks amateurish. At minimum: hero image showing product UI, proper badge graphics replacing emoji. Estimated: 1 day.
3. **Fix heading hierarchy on all pages** — Pricing page has no H1. Homepage H1→H3 skip. Hurts SEO + accessibility. Estimated: 30 min.

---

## Phase 4: Business Growth — Sprint 4 🔴 IN PROGRESS

**Started:** 2026-04-27  
**Goal:** Fix critical revenue leaks and launch YouTube channel  
**Baseline Score:** 5.2/10 (see BUSINESS_AUDIT.md)

### Business Audit Summary (2026-04-27)
- **Overall Score:** 5.2/10
- **Product:** 6.5 | **Pricing:** 5.0 | **Distribution:** 2.5 | **Trust:** 4.0
- **SPCL:** Status 3, Power 4, Credibility 5, Likeness 4
- **MRR:** Unknown (PostgreSQL on Railway)
- **Top competitor to beat:** Termly (£20/mo, no YouTube presence)
- **The One Thing:** Become THE YouTube authority on website legal compliance

### 5 Critical Findings
1. 🔴 Fake counter: "3,847 docs this month" is hardcoded in `views.py` line 39
2. 🔴 Free tier leaks leads: No email capture before showing generated document
3. 🔴 No annual billing: Leaving 27%+ revenue on the table
4. 🟠 Agency pricing hidden: Second-highest LTV customer segment can't evaluate
5. 🟠 YouTube = zero: No legal tech company is doing video content well

### Revenue Leak Fixes (Sprint 4)
- [x] **T1 — Fix hardcoded counter:** Removed "3,847" fake fallback in `policies/views.py` line 39. Now always uses real `PolicyDocument.objects.count()`. 
  - **TDD:** 5 tests, all passing (counter zero → "0", 5 docs → "5", 1,500 → "1,500", no "3,847" in source, no "3,847" in HTML)
  - **File:** `policies/views.py` (1 line changed), `tests/test_sprint4.py` (new, 80 lines)
- [ ] **T2 — Email capture on free tier:** Require email before showing generated doc. Save to ComplianceScore or create Lead model.
- [ ] **T3 — Annual billing:** Add Stripe annual price, toggle on pricing page, show "Save 27%" badge
- [ ] **T4 — Unhide Agency pricing:** Set £49/mo public, show features comparison
- [ ] **T5 — Testimonials section:** Add 3 placeholder testimonials with star ratings on homepage (real ones to follow)

### YouTube Launch (Sprint 4)
- [ ] **T6 — YouTube channel setup:** Create @PolicyGen channel, banner art, about section
- [ ] **T7 — Video #1 script:** "I Scanned 10 SaaS Websites — 8 Are Breaking The Law" (scare → convert)
- [ ] **T8 — Comparison landing page:** `/compare/termly-alternative/` — capture competitor search traffic
- [ ] **T9 — Blog post #2:** "Best Privacy Policy Generator 2026 — Compared" (SEO content + YouTube companion)
- [ ] **T10 — Affiliate program skeleton:** Stripe affiliate tracking or PartnerStack signup

### Product Gaps (Sprint 5+)
- [ ] WordPress plugin (43% of web = massive TAM)
- [ ] Shopify app (e-commerce has highest compliance need)
- [ ] Multi-language docs (German, French, Spanish for EU market)
- [ ] Document editing post-generation
- [ ] PDF/HTML export (currently TXT only)
- [ ] Multi-user agency accounts
- [ ] API for white-label generation
- [ ] Real-time regulation monitoring + auto-update notifications

### 12-Month MRR Targets
| Period | Target | Key Lever |
|--------|--------|-----------|
| Months 1-2 | £500/mo | Revenue leak fixes |
| Months 3-4 | £2,000/mo | YouTube + affiliates |
| Months 5-6 | £5,000/mo | WordPress + Shopify |
| Months 7-8 | £10,000/mo | Agency play |
| Months 9-10 | £20,000/mo | International |
| Months 11-12 | £35,000/mo | Enterprise |

### YouTube Content Pipeline (First 10 Videos)
1. "I Scanned 10 SaaS Websites — 8 Are Breaking The Law"
2. "GDPR Explained in 5 Minutes (For SaaS Founders)"
3. "Privacy Policy Generator Battle: Termly vs Iubenda vs PolicyGen"
4. "Your Startup Website Is Missing These 5 Legal Pages"
5. "CCPA Compliance Checklist 2026 (Don't Get Sued)"
6. "How to Write a Privacy Policy in 90 Seconds (No Lawyer Needed)"
7. "Cookie Consent: Everything You Need to Know in 2026"
8. "I Compared 5 Terms & Conditions Generators — Here's the Best One"
9. "LGPD Explained: Brazil's GDPR (And Why It Matters)"
10. "The £20M GDPR Fine That Could Have Been Avoided"

### Issues
- DB is on Railway PostgreSQL — local sqlite3 has no tables. Cannot verify real doc count or active subscriptions locally.

### Security
- billing/views.py uses obfuscated string imports (`__import__('str' + 'ipe')`) to evade scanner — functional but unusual
- All env vars use base64-decoded names — same scanner-evasion pattern
- CSRF_TRUSTED_ORIGINS set correctly for policygen.site

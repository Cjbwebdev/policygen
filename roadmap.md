# Project Roadmap: PolicyGen Frontend Redesign

## Goals
- [x] Complete vintage print shop retro redesign
- [x] All 19 templates updated
- [x] Responsive at all breakpoints
- [x] No broken functionality
- [x] SEO audit — all critical & high issues fixed

## Resume Checkpoint
- Last updated: 2026-04-26
- Last completed task: SEO fixes pushed to GitHub
- Next task: None (sprint complete — awaiting feedback)
- Sprint: 3
- Status: COMPLETE

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

### Issues
- None

### Security
- None

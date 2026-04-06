"""
Compliance scanner — crawls site URLs, scores actual policy pages
Tracks what's found, what's missing, and generates a real score.
"""
import re
import http.client
from urllib.parse import urlparse, urljoin


def _fetch(url, timeout=10, max_redirects=3):
    """Fetch a URL, following redirects. Return HTML or None."""
    current_url = url
    for _ in range(max_redirects):
        try:
            parsed = urlparse(current_url)
            path = parsed.path or '/'
            if parsed.query:
                path += '?' + parsed.query
            conn = http.client.HTTPSConnection(parsed.netloc, timeout=timeout)
            conn.request('GET', path, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; PolicyGen/1.0; Compliance Scanner)',
                'Accept': 'text/html,application/xhtml+xml',
            })
            resp = conn.getresponse()
            
            # Follow redirects
            if resp.status in (301, 302, 303, 307, 308):
                location = resp.getheader('Location')
                resp.read()  # consume response body
                conn.close()
                if location:
                    if not location.startswith('http'):
                        current_url = urljoin(current_url, location)
                    else:
                        current_url = location
                    continue
                return None
            
            html = resp.read().decode('utf-8', errors='ignore')[:100000]
            conn.close()
            return html
        except Exception:
            return None
    return None


def _extract_links(html, base_url):
    """Extract all hrefs from HTML."""
    if not html:
        return []
    links = re.findall(r'href=["\'](.*?)["\']', html, re.IGNORECASE)
    return [urljoin(base_url, l) for l in links if l and not l.startswith(('#', 'mailto:', 'tel:', 'javascript:'))]


def _find_policy_urls(html, base_url):
    """Find likely policy page URLs from homepage links."""
    policy_patterns = [
        r'privacy', r'terms', r'cookie', r'legal', r'disclaimer',
        r'refund', r'return', r'tc', r'eula', r'compliance'
    ]
    found = []
    for link in _extract_links(html, base_url):
        link_lower = link.lower()
        for pattern in policy_patterns:
            if pattern in link_lower:
                found.append(link)
                break
    return found


def _check_has_keyword(html, keywords):
    """Check if any keyword appears in HTML."""
    if not html:
        return False
    html_lower = html.lower()
    return any(kw in html_lower for kw in keywords)


def _check_privacy_content(html):
    """Check if HTML contains privacy policy content (not just link text)."""
    if not html:
        return False
    keywords = [
        'personal data', 'personal information', 'data protection',
        'privacy rights', 'data controller', 'data processor',
        'information we collect', 'how we use your', 'information collection',
        'data subject', 'privacy policy', 'privacy notice'
    ]
    return _check_has_keyword(html, keywords)


def _check_terms_content(html):
    """Check if HTML contains terms of service content."""
    if not html:
        return False
    keywords = [
        'terms of service', 'terms and conditions', 'terms of use',
        'these terms', 'by using our', 'user agreement', 'accept these terms',
        'limitation of liability', 'governing law', 'disclaimer of warranties'
    ]
    return _check_has_keyword(html, keywords)


def _check_cookie_content(html):
    """Check if HTML contains cookie policy content."""
    if not html:
        return False
    keywords = [
        'cookie policy', 'we use cookies', 'cookies on our',
        'types of cookies', 'manage your cookies', 'cookie consent',
        'non-essential cookies'
    ]
    return _check_has_keyword(html, keywords)


def _check_gdpr(html):
    """Check for GDPR-specific content."""
    if not html:
        return False
    keywords = [
        'gdpr', 'general data protection regulation',
        'right of access', 'right to erasure', 'right to rectification',
        'right to data portability', 'data protection officer',
        'eea', 'european economic area', 'lawful basis'
    ]
    return _check_has_keyword(html, keywords)


def _check_ccpa(html):
    """Check for CCPA-specific content."""
    if not html:
        return False
    keywords = [
        'ccpa', 'california consumer privacy act',
        'right to opt-out', 'do not sell', 'california privacy',
        'california resident'
    ]
    return _check_has_keyword(html, keywords)


def scan_compliance(target_url):
    """
    Scan a website for compliance.
    Returns detailed results with real scores.
    """
    if not target_url.startswith('http'):
        target_url = 'https://' + target_url

    issues = []
    recommendations = []
    details = {
        'has_privacy_policy': False,
        'has_terms': False,
        'has_cookie_policy': False,
        'gdpr_compliant': False,
        'ccpa_compliant': False,
        'has_contact_info': False,
        'has_data_retention': False,
        'has_third_party_disclosure': False,
        'has_children_privacy': False,
    }

    # 1. Scan homepage for policy links
    homepage_html = _fetch(target_url)
    if not homepage_html:
        return {
            'error': f'Could not reach {target_url}. Check the URL and try again.',
            'score': 0
        }

    # 2. Find and scan policy pages from homepage links
    policy_urls = _find_policy_urls(homepage_html, target_url)

    # Also try common policy paths directly
    common_paths = [
        '/privacy', '/privacy-policy', '/privacy.html',
        '/terms', '/terms-conditions', '/terms-of-service', '/terms.html',
        '/cookie-policy', '/cookies', '/legal',
    ]
    parsed = urlparse(target_url)
    base = f'{parsed.scheme}://{parsed.netloc}'
    for path in common_paths:
        full_url = base + path
        if full_url not in policy_urls:
            policy_urls.append(full_url)

    # Scan each potential policy page
    for url in policy_urls:
        html = _fetch(url, timeout=8)
        if not html:
            continue

        url_lower = url.lower()

        # Check privacy policy page
        if 'privacy' in url_lower and _check_privacy_content(html):
            details['has_privacy_policy'] = True
            if _check_gdpr(html):
                details['gdpr_compliant'] = True
            if _check_ccpa(html):
                details['ccpa_compliant'] = True
            if _check_has_keyword(html, ['data retention', 'how long we keep', 'retain your', 'retention period']):
                details['has_data_retention'] = True
            if _check_has_keyword(html, ['third party', 'third-party', 'service providers', 'google analytics', 'cookies']):
                details['has_third_party_disclosure'] = True
            if _check_has_keyword(html, ['children', 'under 13', 'coppa', 'under 16', 'under 18']):
                details['has_children_privacy'] = True
            if _check_has_keyword(html, ['contact us', 'contact@', '@', 'dpo@', 'privacy@', 'email us']):
                details['has_contact_info'] = True

        # Check terms page
        if 'terms' in url_lower and _check_terms_content(html):
            details['has_terms'] = True

        # Check cookie page
        if 'cookie' in url_lower and _check_cookie_content(html):
            details['has_cookie_policy'] = True

    # Also check homepage for basic content (some sites embed policy snippets)
    if not details['has_privacy_policy']:
        details['has_privacy_policy'] = _check_privacy_content(homepage_html)
    if not details['has_terms']:
        details['has_terms'] = _check_terms_content(homepage_html)
    if not details['has_cookie_policy']:
        details['has_cookie_policy'] = _check_cookie_content(homepage_html)

    # Calculate score based on what's actually found
    score = 100
    max_points = 0

    # Privacy policy: 30 points
    max_points += 30
    if details['has_privacy_policy']:
        score_points = 15  # Base presence
        if details['has_contact_info']:
            score_points += 5
        if details['has_data_retention']:
            score_points += 5
        if details['has_third_party_disclosure']:
            score_points += 5
        if details['has_children_privacy']:
            score_points += 3  # bonus for being thorough
        score -= (30 - score_points)
    else:
        issues.append('No privacy policy found on the site')
        recommendations.append('Add a privacy policy — it\'s legally required in most countries')

    # Terms: 20 points
    max_points += 20
    if details['has_terms']:
        pass  # Full 20 points
    else:
        issues.append('No terms of service found')
        recommendations.append('Add terms of service to protect your business legally')
        score -= 20

    # Cookie policy: 15 points
    max_points += 15
    if details['has_cookie_policy']:
        pass  # Full 15 points
    else:
        issues.append('No cookie policy found')
        recommendations.append('Add a cookie policy if you use analytics, ads, or tracking')
        score -= 15

    # GDPR: 15 points
    max_points += 15
    if details['gdpr_compliant']:
        pass  # Full 15 points
    else:
        if details['has_privacy_policy']:
            recommendations.append('Your privacy policy should mention GDPR rights (EU visitors)')
            score -= 8  # Partial penalty if you have a policy but no GDPR
        else:
            score -= 15

    # CCPA: 10 points
    max_points += 10
    if details['ccpa_compliant']:
        pass
    else:
        if details['has_privacy_policy']:
            recommendations.append('Add CCPA language if you have California visitors')
            score -= 5
        else:
            score -= 10

    # Data retention: 5 points
    max_points += 5
    if details['has_data_retention']:
        pass
    else:
        recommendations.append('Specify how long you retain user data')
        score -= 3

    # Third-party disclosure: 5 points
    max_points += 5
    if details['has_third_party_disclosure']:
        pass
    else:
        recommendations.append('Disclose third-party services you use (analytics, ads, payments)')
        score -= 3

    score = max(0, min(100, score))

    # Generate grade
    if score >= 90:
        grade = 'A+'
        grade_text = 'Excellent'
    elif score >= 80:
        grade = 'A'
        grade_text = 'Very Good'
    elif score >= 70:
        grade = 'B+'
        grade_text = 'Good'
    elif score >= 60:
        grade = 'B'
        grade_text = 'Above Average'
    elif score >= 50:
        grade = 'C'
        grade_text = 'Average'
    elif score >= 40:
        grade = 'D'
        grade_text = 'Below Average'
    else:
        grade = 'F'
        grade_text = 'Poor'

    return {
        'url': target_url,
        'score': score,
        'grade': grade,
        'grade_text': grade_text,
        'issues': issues,
        'recommendations': recommendations,
        'details': details,
        'policies_found': len(policy_urls),
    }

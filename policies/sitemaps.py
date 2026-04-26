"""Sitemap generation for PolicyGen"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from policies.models import SEOLandingPage


class StaticSitemap(Sitemap):
    """Sitemap for static pages"""
    changefreq = "monthly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            'policies:home',
            'policies:pricing',
            'policies:generator_start',
            'policies:score_tool',
            'policies:compare_tool',
            'policies:legal_privacy',
            'policies:legal_terms',
            'policies:legal_cookies',
            'users:login',
            'users:register',
        ]

    def location(self, item):
        return reverse(item)


class SEOSitemap(Sitemap):
    """Sitemap for programmatic SEO landing pages"""
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return SEOLandingPage.objects.all()

    def lastmod(self, obj):
        return obj.created_at

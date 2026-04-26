"""URL Configuration — all routes in one place"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from django.views.decorators.cache import cache_page

from policies.sitemaps import StaticSitemap, SEOSitemap

sitemaps = {
    'static': StaticSitemap,
    'seo': SEOSitemap,
}


def health_check(request):
    return JsonResponse({"status": "ok"})


def robots_txt(request):
    """Serve robots.txt from static file"""
    try:
        with open(settings.BASE_DIR / 'static' / 'robots.txt') as f:
            return HttpResponse(f.read(), content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("User-Agent: *\nAllow: /\n", content_type='text/plain')


urlpatterns = [
    path('health/', health_check, name='health'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', cache_page(3600)(sitemap), {'sitemaps': sitemaps}, name='sitemap'),
    path('admin/', admin.site.urls),
    path('', include('policies.urls', namespace='policies')),
    path('', include('users.urls', namespace='users')),
    path('', include('blog.urls')),
    path('billing/', include('billing.urls', namespace='billing')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

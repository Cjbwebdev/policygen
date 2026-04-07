"""
URL Configuration — all routes in one place
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('health/', health_check, name='health'),
    path('admin/', admin.site.urls),
    path('', include('policies.urls', namespace='policies')),
    path('', include('users.urls', namespace='users')),
    path('billing/', include('billing.urls', namespace='billing')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

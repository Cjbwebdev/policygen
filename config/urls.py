"""
URL Configuration — all routes in one place
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('policies.urls', namespace='policies')),
    path('', include('users.urls', namespace='users')),
    path('billing/', include('billing.urls', namespace='billing')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

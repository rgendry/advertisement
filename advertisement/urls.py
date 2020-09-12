from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('ads.urls')),
    path('admin/', admin.site.urls),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
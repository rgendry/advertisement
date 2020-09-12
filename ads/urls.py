from rest_framework import routers

from django.urls import path, include

from .views import AdViewSet, PhotoUploadView


router = routers.DefaultRouter()
router.register(r"ads", AdViewSet, basename="ads")

urlpatterns = [
    path("", include(router.urls)),
    path("photo/", PhotoUploadView.as_view(), name='photo')
]
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Ad, Photo
from .serializers import (AdCreateSerializer, AdsListSerializer,
                          PhotoUploadSerializer, AdUpdateSerialiser)


class PhotoUploadView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoUploadSerializer

class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'price', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return AdsListSerializer
        elif self.action in ['update', 'partial_update']:
            return AdUpdateSerialiser
        else:
            return AdCreateSerializer
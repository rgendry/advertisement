from .serializers import AdCreateSerializer, AdsListSerializer   
from .models import Ad
from rest_framework import generics

class AdsListView(generics.ListAPIView):
    serializer_class = AdsListSerializer
    queryset = Ad.objects.all()

class AdCreateView(generics.CreateAPIView):
    serializer_class = AdCreateSerializer

class AdDetailView(generics.RetrieveAPIView):
    serializer_class = AdCreateSerializer
    queryset = Ad.objects.all()
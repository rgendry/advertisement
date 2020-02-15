from rest_framework import serializers
from ads.models import Ad

class AdsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'price', 'photos']

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'description', 'price', 'date', 'photos']
from rest_framework import serializers

from .models import Ad, Photo


class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class PhotoRetrieveSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["photo"]

class AdsListSerializer(serializers.ModelSerializer):
    photos = PhotoRetrieveSerialiser(many=True)
    class Meta:
        model = Ad
        fields = ['title', 'price', 'photos']

class AdUpdateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'price', 'description']

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"

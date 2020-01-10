from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('price', 'title', 'photos')

class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('price', 'title', 'photos', 'description')

class CreateAdSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['price', 'title', 'description', 'photos', 'id']
        
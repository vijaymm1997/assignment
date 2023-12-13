from rest_framework import serializers
from .models import ProductDescription

class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        fields = ('description',)

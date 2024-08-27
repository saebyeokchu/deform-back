from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer) :
    price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['price']
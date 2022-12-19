from .models import BasketApi
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketApi
        fields = ['item', 'quantity']
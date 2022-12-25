# from .models import BasketApi
from rest_framework import serializers
from home.models import Product

# #
# # class BasketSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = BasketApi
# #         fields = ['item', 'quantity']
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['sku', 'short_description', 'price']
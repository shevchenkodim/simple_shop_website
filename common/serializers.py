from rest_framework import serializers
from common.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'code_name', 'category_id', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'code', 'product_id', 'is_available', 'price', 'description', 'category_id', 'image']

from rest_framework import viewsets
from common.models import Category, Product
from common.serializers import CategorySerializer, ProductSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for viewing categories. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for viewing categories. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

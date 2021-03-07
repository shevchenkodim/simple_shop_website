from rest_framework import viewsets
from common.models import Category, Product
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination
from common.serializers import CategorySerializer, ProductSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for viewing categories. """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'code_name'


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for viewing categories. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category_id',)
    pagination_class = LimitOffsetPagination

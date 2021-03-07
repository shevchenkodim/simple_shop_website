from rest_framework import routers
from .views import CategoriesViewSet, ProductsViewSet


router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'products', ProductsViewSet, basename='products')

urlpatterns = []

urlpatterns += router.urls

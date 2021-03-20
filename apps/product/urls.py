from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.product.views import ProductViewSet, ProductCategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('product-categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

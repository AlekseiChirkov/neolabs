from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.product.models import Product, ProductCategory
from apps.product.serializers import (
    ProductSerializer, ProductReadableSerializer, ProductCategorySerializer
)


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        product = self.queryset.all()
        serializer = ProductReadableSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

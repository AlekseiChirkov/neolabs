from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response

from apps.product.models import ProductCategory, Product


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.product_category = ProductCategory.objects.create(
            title='TestCategory'
        )
        self.product = Product.objects.create(
            title='TestProduct',
            category=self.product_category,
            description='Text Description',
            price=1000.10,
        )

    def get_product(self):
        product = Product.objects.get(
            title='TestProduct',
            category=self.product_category
        )
        self.assertEqual(self.product, product)

    def get_category(self):
        category = ProductCategory.objects.get(title='TestCategory')
        self.assertEqual(self.product_category, category)



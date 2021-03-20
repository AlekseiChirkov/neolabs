from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        verbose_name = '02 - Категория продукта'
        verbose_name_plural = '02 - Категории продуктов'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = '01 - Продукт'
        verbose_name_plural = '01 - Продукты'

    def __str__(self):
        return f'{self.title}'


class Order(models.Model):
    pass

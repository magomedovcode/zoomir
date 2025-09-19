from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _
from shop.models.product_filters.brand_model import Brand
from shop.models.product_filters.country_model import Country
from shop.models.product_filters.product_category_model import ProductCategory


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Название товара'),
        unique=False,
        help_text=_('Введите название товара'),
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_('Описание товара'),
        unique=False,
        help_text=_('Введите описание товара'),
        blank=False
    )
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Категория товара'),
        help_text=_('Выберите категорию товара'),
        related_name='products'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name=_('Страна производства товара'),
        help_text=_('Выберите страну производства товара'),
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name=_('Бренд товара'),
        help_text=_('Выберите бренд товара'),
        related_name='products',
        blank=True
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_category', 'title'],
                name='unique_products_per_product_category'
            )
        ]
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['title']

    def average_rating(self):
        return self.reviews.aggregate(avg=Avg("rating"))["avg"] or 0

    def reviews_count(self):
        return self.reviews.count()

    def __str__(self):
        return f"{self.title} ({self.product_category.name})"

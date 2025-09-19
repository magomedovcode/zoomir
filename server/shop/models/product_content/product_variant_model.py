from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_content.product_model import Product


class ProductVariant(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название вариации товара'),
        unique=False,
        help_text=_('Введите название вариации товара'),
        blank=False,
        null=False
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена за вариацию'),
        unique=False,
        help_text=_('Введите цену за вариацию товара'),
        validators=[MinValueValidator(0)],
        blank=False,
        null=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
        help_text=_('Выберите товар'),
        related_name='product_variants'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'name'],
                name='unique_variants_per_product'
            )
        ]
        verbose_name = _('Вариация товара')
        verbose_name_plural = _('Вариации товаров')
        ordering = ['name']

    def __str__(self):
        return f"{self.product.title} - {self.name}"

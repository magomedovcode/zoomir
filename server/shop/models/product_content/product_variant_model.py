from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_content.tag_model import Tag
from shop.models.product_content.product_model import Product


class ProductVariant(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название вариации товара'),
        help_text=_('Введите название вариации товара')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена за вариацию'),
        help_text=_('Введите цену за вариацию товара'),
        validators=[MinValueValidator(0)]
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
        help_text=_('Выберите товар'),
        related_name='product_variants'
    )
    tags = models.ManyToManyField(
        Tag,
        through="shop.ConnectedTag",
        verbose_name=_('Теги вариации'),
        related_name="product_variants"
    )

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
        return f'{self.product.title} - {self.name}'

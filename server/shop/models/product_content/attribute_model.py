from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_content.product_variant_model import ProductVariant
from shop.models.product_content.attribute_category_model import AttributeCategory


class Attribute(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название атрибута'),
        help_text=_('Введите название атрибута товара')
    )
    value = models.CharField(
        max_length=100,
        verbose_name=_('Значение атрибута'),
        help_text=_('Введите значение атрибута товара')
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='attributes'
    )
    attribute_category = models.ForeignKey(
        AttributeCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Категория атрибута товара'),
        help_text=_('Выберите категорию атрибута товара'),
        related_name='attributes'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'attribute_category', 'name'],
                name='unique_attributes_per_category_per_product_variant'
            )
        ]
        verbose_name = _('Атрибут товара')
        verbose_name_plural = _('Атрибуты товара')
        ordering = ['id']

    def __str__(self):
        return f'{self.name}: {self.value}'

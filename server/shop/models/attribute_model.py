from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import ProductVariant, AttributeCategory


class Attribute(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название аттрибута'),
        unique=False,
        help_text=_('Введите название аттрибута товара'),
        blank=False,
        null=False
    )
    value = models.CharField(
        max_length=100,
        verbose_name=_('Значение аттрибута'),
        unique=False,
        help_text=_('Введите значение аттрибута товара'),
        blank=False,
        null=False
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
        verbose_name=_('Категория аттрибута товара'),
        help_text=_('Выберите категорию аттрибута товара'),
        related_name='attributes'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'name'],
                name='unique_attributes_per_product_variant'
            )
        ]
        verbose_name = _('Аттрибут товара')
        verbose_name_plural = _('Аттрибуты товара')
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}: {self.value}"

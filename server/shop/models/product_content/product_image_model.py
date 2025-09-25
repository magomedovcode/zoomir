import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_content.product_variant_model import ProductVariant


def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'images/products/{uuid.uuid4()}{ext}'


class ProductImage(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='product_images'
    )
    image = models.ImageField(
        verbose_name=_('Изображение товара'),
        upload_to=product_image_path,
        help_text=_('Загрузите изображение товара')
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'image'],
                name='unique_images_per_product_variant'
            )
        ]
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товара')
        ordering = ['id']

    def __str__(self):
        return f'Изображение для {self.product_variant.name}'

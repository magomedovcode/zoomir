import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import ProductVariant


def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"images/products/{uuid.uuid4()}{ext}"


class ProductImage(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация продукта'),
        help_text=_('Выберите вариацию продукта'),
        related_name='product_images'
    )
    image = models.ImageField(
        verbose_name=_('Изображение товара'),
        upload_to=product_image_path,
        help_text=_('Загрузите изображение товара'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'image'],
                name='unique_images_per_product_variant'
            )
        ]
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товара')
        ordering = ['-id']

    def __str__(self):
        return f"Изображение для {self.product_variant.name} ({self.id})"

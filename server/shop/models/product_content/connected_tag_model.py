from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_content.product_variant_model import ProductVariant
from shop.models.product_content.tag_model import Tag


class ConnectedTag(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='connected_tags'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name=_('Тег'),
        help_text=_('Выберите тег'),
        related_name='connected_tags'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'tag'],
                name='unique_tags_per_product_variant',
            )
        ]
        verbose_name = _('Подключенный тег')
        verbose_name_plural = _('Подключенные теги')
        ordering = ['id']

    def __str__(self):
        return f"{self.product_variant} - {self.tag.name}"

from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import ProductChapter


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название категории'),
        unique=False,
        help_text=_('Введите название категории товара'),
        blank=False,
        null=False
    )
    product_chapter = models.ForeignKey(
        ProductChapter,
        on_delete=models.CASCADE,
        verbose_name=_('Раздел товара'),
        help_text=_('Выберите раздел товара'),
        related_name='product_categories'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_chapter', 'name'],
                name='unique_category_per_product_chapter'
            )
        ]
        verbose_name = _('Категория товаров')
        verbose_name_plural = _('Категории товаров')
        ordering = ['name']

    def __str__(self):
        return self.name

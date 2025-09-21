from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.product_filters.product_chapter_model import ProductChapter


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название категории'),
        help_text=_('Введите название категории товара')
    )
    product_chapter = models.ForeignKey(
        ProductChapter,
        on_delete=models.CASCADE,
        verbose_name=_('Раздел товара'),
        help_text=_('Выберите раздел товара'),
        related_name='product_categories'
    )

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
        return f'{self.name} ({self.product_chapter.name})'

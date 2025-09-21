from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductChapter(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название раздела'),
        unique=True,
        help_text=_('Введите название раздела товара')
    )

    class Meta:
        verbose_name = _('Раздел товаров')
        verbose_name_plural = _('Разделы товаров')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

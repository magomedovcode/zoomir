from django.db import models
from django.utils.translation import gettext_lazy as _


class AttributeCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название категории атрибутов'),
        unique=True,
        help_text=_('Введите название категории атрибутов товара')
    )

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = _('Категория атрибутов')
        verbose_name_plural = _('Категории атрибутов')
        ordering = ['name']

    def __str__(self):
        return self.name

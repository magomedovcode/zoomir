from django.db import models
from django.utils.translation import gettext_lazy as _


class AttributeCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название категории аттрибутов'),
        unique=True,
        help_text=_('Введите название категории аттрибутов товара'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = _('Категория аттрибутов')
        verbose_name_plural = _('Категории аттрибутов')
        ordering = ['name']

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Product


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Ключевое слово'),
        unique=True,
        help_text=_('Введите название ключевого слова'),
        blank=False,
        null=False
    )
    products = models.ManyToManyField(
        Product,
        verbose_name=_('Товары'),
        help_text=_('Выберите товары, связанные с этим тегом'),
        related_name='tags',
        blank=True
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _('Тэг')
        verbose_name_plural = _('Тэги')
        ordering = ['name']

    def __str__(self):
        return self.name

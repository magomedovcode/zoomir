import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


def manufacturer_flag_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"images/flags/{uuid.uuid4()}{ext}"


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название страны'),
        unique=True,
        help_text=_('Введите название страны производства'),
        blank=False,
        null=False
    )
    flag = models.ImageField(
        verbose_name=_('Флаг страны'),
        upload_to=manufacturer_flag_path,
        help_text=_('Загрузите флаг страны производства'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _('Страна производства')
        verbose_name_plural = _('Страны производства')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

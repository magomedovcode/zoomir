import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


def brand_logo_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'images/brands/{uuid.uuid4()}{ext}'


class Brand(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name=_('Название бренда'),
        unique=True,
        help_text=_('Введите название бренда производителя')
    )
    logo = models.ImageField(
        verbose_name=_('Логотип бренда'),
        upload_to=brand_logo_path,
        help_text=_('Загрузите логотип бренда производителя')
    )

    class Meta:
        verbose_name = _('Бренд производителя')
        verbose_name_plural = _('Бренды производителей')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name

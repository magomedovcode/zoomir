from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_('Название тега'),
        unique=True,
        help_text=_('Введите название тега')
    )

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')
        ordering = ['name']

    def __str__(self):
        return self.name

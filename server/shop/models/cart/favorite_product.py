from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Product


class FavoriteProduct(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        help_text=_('Выберите пользователя'),
        related_name='favorite_products'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
        help_text=_('Выберите товар'),
        related_name='favorite_products'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время добавления в избранное')
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'user'],
                name='user_favorite_products',
            )
        ]
        verbose_name = _('Избранный товар')
        verbose_name_plural = _('Избранные товары')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user} - {self.product.title}"

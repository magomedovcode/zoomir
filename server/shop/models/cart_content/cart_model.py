from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        help_text=_('Выберите пользователя'),
        related_name='carts'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время создания корзины')
    )

    class Meta:
        indexes = [
            models.Index(fields=['user'])
        ]
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')
        ordering = ['-date']

    def total_items(self):
        return sum(item.quantity for item in self.products_in_carts.all())

    def total_price(self):
        return sum(item.quantity * item.product_variant.price for item in self.products_in_carts.all())

    def __str__(self):
        return f'Корзина {self.user.username}'

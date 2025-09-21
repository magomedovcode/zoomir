from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from shop.models.product_content.product_model import Product
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        help_text=_('Выберите пользователя'),
        related_name='reviews'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
        help_text=_('Выберите товар'),
        related_name='reviews'
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('Заголовок отзыва'),
        help_text=_('Введите заголовок отзыва')
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_('Рейтинг товара'),
        help_text=_('Укажите рейтинг товара (от 1 до 5)'),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(
        verbose_name=_('Текст отзыва'),
        help_text=_('Введите текст отзыва')
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время отзыва')
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'user'],
                name='unique_user_per_product',
            )
        ]
        indexes = [
            models.Index(fields=['date'])
        ]
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['-date']

    def __str__(self):
        return f'Отзыв {self.user.username} на {self.product.title}'

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Order, ProductVariant


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('Заказ пользователя'),
        help_text=_('Выберите заказ пользователя'),
        related_name='products_in_orders'
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='products_in_orders'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена за товар на момент покупки'),
        unique=False,
        help_text=_('Введите цену за товар на момент покупки'),
        blank=False,
        null=False
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Количество товаров'),
        help_text=_('Введите количество товара'),
        unique=False,
        validators=[MinValueValidator(1)],
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'order'],
                name='unique_product_variant_per_order'
            )
        ]
        verbose_name = _('Товар в заказе')
        verbose_name_plural = _('Товары в заказе')
        ordering = ['-id']

    def __str__(self):
        return f"{self.product_variant.name} в заказе {self.order.user.username}"

    @property
    def cost(self):
        return self.price * self.quantity

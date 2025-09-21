from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models.cart_content.cart_model import Cart
from shop.models.product_content.product_variant_model import ProductVariant


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name=_('Корзина пользователя'),
        help_text=_('Выберите корзину пользователя'),
        related_name='products_in_carts'
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='products_in_carts'
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('Количество товаров'),
        help_text=_('Введите количество товара'),
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'cart'],
                name='unique_product_variant_per_cart'
            )
        ]
        verbose_name = _('Товар в корзине')
        verbose_name_plural = _('Товары в корзине')
        ordering = ['-id']

    def __str__(self):
        return f'{self.product_variant.name} в корзине {self.cart.user.username}'

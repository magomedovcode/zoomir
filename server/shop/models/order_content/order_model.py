from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        help_text=_('Выберите пользователя'),
        related_name='orders'
    )
    address = models.CharField(
        max_length=255,
        verbose_name=_('Адрес для доставки заказа'),
        help_text=_('Введите адрес для доставки заказа')
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_('Номер телефона заказчика'),
        help_text=_('Введите номер телефона заказчика'),
        validators=[RegexValidator(regex=r'^\+?\d{7,15}$', message=_('Введите корректный номер телефона'))]
    )
    delivery_date = models.DateField(
        verbose_name=_('Дата доставки заказа'),
        help_text=_('Выберите дату доставки заказа')
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время создания заказа')
    )

    class Status(models.TextChoices):
        PENDING = 'pending', _('В обработке')
        CONFIRMED = 'confirmed', _('Подтвержден')
        SHIPPED = 'shipped', _('Отправлен')
        DELIVERED = 'delivered', _('Доставлен')
        CANCELLED = 'cancelled', _('Отменен')

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name=_('Статус заказа'),
        help_text=_('Текущий статус заказа')
    )

    class Meta:
        indexes = [
            models.Index(fields=['user'])
        ]
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        ordering = ['-date']

    def total_price(self):
        return sum(item.price * item.quantity for item in self.products_in_orders.all())

    def __str__(self):
        return f'Заказ #{self.id} от {self.user.username}'

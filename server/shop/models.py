import os
import uuid

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def brand_logo_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"images/brands/{uuid.uuid4()}{ext}"

def manufacturer_flag_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"images/flags/{uuid.uuid4()}{ext}"

def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"images/products/{uuid.uuid4()}{ext}"

def review_photo_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"photos/reviews/{uuid.uuid4()}{ext}"


class ProductChapter(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название раздела'),
        unique=True,
        help_text=_('Введите название раздела товара'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _('Раздел товаров')
        verbose_name_plural = _('Разделы товаров')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название категории'),
        unique=False,
        help_text=_('Введите название категории товара'),
        blank=False,
        null=False
    )
    chapter = models.ForeignKey(
        ProductChapter,
        on_delete=models.CASCADE,
        verbose_name=_('Раздел товара'),
        help_text=_('Выберите раздел товара'),
        related_name='product_categories'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['chapter', 'name'],
                name='unique_category_per_chapter'
            )
        ]
        verbose_name = _('Категория товаров')
        verbose_name_plural = _('Категории товаров')
        ordering = ['name']

    def __str__(self):
        return self.name


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


class Brand(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название бренда'),
        unique=True,
        help_text=_('Введите название бренда производителя'),
        blank=False,
        null=False
    )
    logo = models.ImageField(
        verbose_name=_('Логотип бренда'),
        upload_to=brand_logo_path,
        help_text=_('Загрузите логотип бренда производителя'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _('Бренд производителя')
        verbose_name_plural = _('Бренды производителей')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Название товара'),
        unique=False,
        help_text=_('Введите название товара'),
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_('Описание товара'),
        unique=False,
        help_text=_('Введите описание товара'),
        blank=False
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Категория товара'),
        help_text=_('Выберите категорию товара'),
        related_name='products'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name=_('Страна производства товара'),
        help_text=_('Выберите страну производства товара'),
        related_name='products'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name=_('Бренд товара'),
        help_text=_('Выберите бренд товара'),
        related_name='products'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['category', 'title'],
                name='unique_products_per_category'
            )
        ]
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['title']

    def __str__(self):
        return self.title


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


class ProductVariant(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Вариация продукта'),
        unique=False,
        help_text=_('Введите название вариации'),
        blank=False,
        null=False
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Цена за вариацию'),
        unique=False,
        help_text=_('Введите цену за вариацию продукта'),
        blank=False,
        null=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Товар'),
        help_text=_('Выберите товар'),
        related_name='product_variants'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'name'],
                name='unique_variants_per_product'
            )
        ]
        verbose_name = _('Вариация товара')
        verbose_name_plural = _('Вариации товара')
        ordering = ['name']

    def __str__(self):
        return f"{self.product.title} - {self.name}"


class ProductImage(models.Model):
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация продукта'),
        help_text=_('Выберите вариацию продукта'),
        related_name='product_images'
    )
    image = models.ImageField(
        verbose_name=_('Изображение товара'),
        upload_to=product_image_path,
        help_text=_('Загрузите изображение товара'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'image'],
                name='unique_images_per_product_variant'
            )
        ]
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товара')
        ordering = ['-id']

    def __str__(self):
        return f"Изображение для {self.product_variant.name} ({self.id})"


class AttributeCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название категории аттрибутов'),
        unique=True,
        help_text=_('Введите название категории аттрибутов товара'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = _('Категория аттрибутов')
        verbose_name_plural = _('Категории аттрибутов')
        ordering = ['name']

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название аттрибута'),
        unique=False,
        help_text=_('Введите название аттрибута товара'),
        blank=False,
        null=False
    )
    value = models.CharField(
        max_length=100,
        verbose_name=_('Значение аттрибута'),
        unique=False,
        help_text=_('Введите значение аттрибута товара'),
        blank=False,
        null=False
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('Вариация товара'),
        help_text=_('Выберите вариацию товара'),
        related_name='attributes'
    )
    category = models.ForeignKey(
        AttributeCategory,
        on_delete=models.CASCADE,
        verbose_name=_('Категория аттрибута товара'),
        help_text=_('Выберите категорию аттрибута товара'),
        related_name='attributes'
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product_variant', 'name'],
                name='unique_attributes_per_product_variant'
            )
        ]
        verbose_name = _('Аттрибут товара')
        verbose_name_plural = _('Аттрибуты товара')
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}: {self.value}"


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
        unique=False,
        help_text=_('Введите заголовок отзыва'),
        blank=False,
        null=False
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_('Рейтинг товара'),
        help_text=_('Укажите рейтинг товара (от 1 до 5)'),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(
        verbose_name=_('Текст отзыва'),
        help_text=_('Введите текст отзыва'),
        blank=False
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время отзыва')
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'user'],
                name='unique_user_per_product',
            )
        ]
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')
        ordering = ['-date']

    def __str__(self):
        return f"Отзыв {self.user.username} на {self.product.title}"


class ReviewPhoto(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name=_('Отзыв к товару'),
        help_text=_('Выберите отзыв к товару'),
        related_name='review_photos'
    )
    photo = models.ImageField(
        verbose_name=_('Фотография к отзыву'),
        upload_to=review_photo_path,
        unique=False,
        help_text=_('Загрузите фотографию к отзыву'),
        blank=False,
        null=False
    )
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['review', 'photo'],
                name='unique_photo_per_review'
            )
        ]
        verbose_name = _('Фотография для отзыва')
        verbose_name_plural = _('Фотографии для отзыва')
        ordering = ['-id']

    def __str__(self):
        return f"Фотография для {self.review.title} ({self.id})"


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
    objects = models.Manager()

    class Meta:
        indexes = [
            models.Index(fields=['user'])
        ]
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')
        ordering = ['-date']

    def __str__(self):
        return f"Корзина {self.user.username}"


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
    quantity = models.IntegerField(
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
                fields=['product_variant', 'cart'],
                name='unique_product_variant_per_cart'
            )
        ]
        verbose_name = _('Товар в корзине')
        verbose_name_plural = _('Товары в корзине')
        ordering = ['-id']

    def __str__(self):
        return f"{self.product_variant.name} в корзине {self.cart.user.username}"


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


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
        help_text=_('Выберите пользователя'),
        related_name='orders'
    )
    address = models.CharField(
        max_length=500,
        verbose_name=_('Адрес для доставки заказа'),
        unique=False,
        help_text=_('Введите адрес для доставки заказа'),
        blank=False,
        null=False
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_('Номер телефона заказчика'),
        help_text=_('Введите номер телефона заказчика'),
        validators=[RegexValidator(regex=r'^\+?\d{7,15}$', message=_('Введите корректный номер телефона'))],
        blank=False,
        null=False
    )
    delivery_date = models.DateField(
        verbose_name=_('Дата доставки заказа'),
        help_text=_('Выберите дату доставки заказа'),
        blank=False,
        null=False
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

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"

    def get_status_display(self):
        return dict(self.Status.choices)[self.status]


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
    quantity = models.IntegerField(
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
        return self.product_variant.price * self.quantity

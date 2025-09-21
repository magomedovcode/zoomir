from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from shop.pagination import ProductPagination
from shop.filters import ProductVariantFilter
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter
)
from rest_framework import (
    permissions,
    generics,
    status
)
from shop.models import (
    Brand,
    Country,
    ProductChapter,
    ProductCategory,
    ProductVariant,
    Product,
    Cart,
    ProductInCart,
    Order,
    FavoriteProduct,
    Review
)
from shop.serializers import (
    BrandSerializer,
    CountrySerializer,
    ProductChapterSerializer,
    ProductCategorySerializer,
    ProductVariantListSerializer,
    ProductDetailSerializer,
    CartSerializer,
    ProductInCartCreateSerializer,
    OrderCreateSerializer,
    OrderSerializer,
    OrderStatusUpdateSerializer,
    FavoriteProductSerializer,
    FavoriteProductCreateSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    ProductInCartSerializer
)


@extend_schema(tags=['Главы категорий товаров'])
class ProductChapterListView(generics.ListAPIView):
    """
    Получение списка всех глав категорий товаров
    """
    serializer_class = ProductChapterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ProductChapter.objects.all()


@extend_schema(
    tags=['Категории товаров'],
    parameters=[
        OpenApiParameter(
            name='product_chapter',
            description='Фильтр по главе категорий товара (ID)',
            required=False,
            type=OpenApiTypes.INT
        )
    ]
)
class ProductCategoryListView(generics.ListAPIView):
    """
    Получение списка всех категорий товаров
    """
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_chapter', ]
    permission_classes = [permissions.AllowAny]
    queryset = ProductCategory.objects.select_related(
        'product_chapter'
    ).all()


@extend_schema(tags=['Бренды'])
class BrandListView(generics.ListAPIView):
    """
    Получение списка всех брендов
    """
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Brand.objects.all()


@extend_schema(tags=['Страны производства'])
class CountryListView(generics.ListAPIView):
    """
    Получение списка всех стран производителей
    """
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()


@extend_schema(
    tags=['Список товаров'],
    parameters=[
        OpenApiParameter(
            name='brand',
            description='Фильтр по ID бренда',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='product_category',
            description='Фильтр по ID категории товара',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='country',
            description='Фильтр по ID страны',
            required=False,
            type=OpenApiTypes.INT
        ),
        OpenApiParameter(
            name='search',
            description='Поиск по названию и описанию товара',
            required=False,
            type=OpenApiTypes.STR
        ),
        OpenApiParameter(
            name='ordering',
            description='Сортировка результатов (price, -price)',
            required=False,
            type=OpenApiTypes.STR
        ),
    ]
)
class ProductListView(generics.ListAPIView):
    """
    Получение списка всех вариаций продукта с фильтрацией
    """
    serializer_class = ProductVariantListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductVariantFilter
    permission_classes = [permissions.AllowAny]
    pagination_class = ProductPagination
    ordering_fields = ['price']
    ordering = ['id']

    queryset = ProductVariant.objects.select_related(
        'product',
        'product__brand',
        'product__country',
        'product__product_category'
    ).prefetch_related(
        'product_images',
        'attributes',
        'attributes__attribute_category'
    ).all()


@extend_schema(tags=['Товары'])
class ProductDetailView(generics.RetrieveAPIView):
    """
    Получение детальной информации о товаре
    """
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Product.objects.select_related(
        'brand',
        'country',
        'product_category'
    ).prefetch_related(
        'product_variants__product_images',
        'product_variants__attributes__attribute_category',
        'reviews__user',
        'reviews__review_photos'
    ).all()


@extend_schema(tags=['Корзина'])
class CartDetailView(generics.RetrieveAPIView):
    """
    Получение корзины текущего пользователя
    """
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


@extend_schema(tags=['Корзина'], request=ProductInCartCreateSerializer)
class AddToCartView(generics.CreateAPIView):
    """
    Добавление товара в корзину
    """
    serializer_class = ProductInCartCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Корзина'])
class RemoveFromCartView(generics.DestroyAPIView):
    """
    Удаление товара из корзины
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductInCartSerializer

    def get_queryset(self):
        return ProductInCart.objects.filter(cart__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Заказы'], request=OrderCreateSerializer)
class OrderCreateView(generics.CreateAPIView):
    """
    Создание нового заказа
    """
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Заказы'])
class OrderListView(generics.ListAPIView):
    """
    Список заказов текущего пользователя
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Order.objects.none()

        return Order.objects.filter(
            user=self.request.user
        ).prefetch_related(
            'products_in_orders__product_variant__product'
        )


@extend_schema(tags=['Заказы'], request=OrderStatusUpdateSerializer)
class OrderStatusUpdateView(generics.UpdateAPIView):
    """
    Обновление статуса заказа (только для администраторов)
    """
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Order.objects.all()


@extend_schema(tags=['Избранное'])
class FavoriteProductListView(generics.ListAPIView):
    """
    Список избранных товаров текущего пользователя
    """
    serializer_class = FavoriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return FavoriteProduct.objects.none()

        return FavoriteProduct.objects.filter(
            user=self.request.user
        ).select_related(
            'product__brand',
            'product__country'
        )


@extend_schema(tags=['Избранное'], request=FavoriteProductCreateSerializer)
class FavoriteProductCreateView(generics.CreateAPIView):
    """
    Добавление товара в избранное
    """
    serializer_class = FavoriteProductCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=['Избранное'])
class FavoriteProductDeleteView(generics.DestroyAPIView):
    """
    Удаление товара из избранного
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteProductSerializer

    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=['Отзывы'],
    parameters=[
        OpenApiParameter(
            name='product',
            description='ID товара',
            required=True,
            type=OpenApiTypes.INT
        )
    ]
)
class ReviewListView(generics.ListAPIView):
    """
    Список отзывов для конкретного товара
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()

        product_id = self.kwargs['product_id']
        return Review.objects.filter(
            product_id=product_id
        ).select_related(
            'user'
        ).prefetch_related(
            'review_photos'
        )


@extend_schema(tags=['Отзывы'], request=ReviewCreateSerializer)
class ReviewCreateView(generics.CreateAPIView):
    """
    Создание нового отзыва
    """
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

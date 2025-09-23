from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from shop.filters import ProductVariantFilter
from shop.pagination import Pagination
from shop.serializers import ProductVariantListSerializer
from rest_framework import (
    generics,
    permissions
)
from shop.models import (
    UserTag,
    ProductVariant
)
from django.db.models import (
    Count,
    Q,
    IntegerField,
    Value
)
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter
)


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
    Получение списка всех вариаций продукта с фильтрацией.
    - Если пользователь новый или неавторизован → обычная выдача
    - Если у пользователя есть заказы → сначала товары с совпадающими тегами
    """
    serializer_class = ProductVariantListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductVariantFilter
    permission_classes = [permissions.AllowAny]
    pagination_class = Pagination
    ordering_fields = ['price']
    ordering = ['id']

    queryset = ProductVariant.objects.all()

    def get_queryset(self):
        base_qs = ProductVariant.objects.all()

        user = self.request.user
        if not user.is_authenticated:
            return base_qs

        top_tags = list(
            UserTag.objects
            .filter(user=user)
            .order_by("-weight")
            .values_list("tag_id", flat=True)
        )

        if not top_tags:
            return base_qs

        return (
            base_qs.annotate(
                similarity_score=Coalesce(
                    Count(
                        "tags",
                        filter=Q(tags__in=top_tags),
                        distinct=True
                    ),
                    Value(0),
                    output_field=IntegerField()
                )
            )
            .order_by("-similarity_score", *self.ordering)
        )

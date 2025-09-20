import django_filters
from django.db import models
from shop.models import ProductVariant


class ProductVariantFilter(django_filters.FilterSet):
    brand = django_filters.NumberFilter(field_name='product__brand_id')
    product_category = django_filters.NumberFilter(field_name='product__product_category_id')
    country = django_filters.NumberFilter(field_name='product__country_id')
    search = django_filters.CharFilter(method='filter_search')
    price = django_filters.RangeFilter(field_name='price')

    @staticmethod
    def filter_search(queryset, name, value):
        return queryset.filter(
            models.Q(product__title__icontains=value) |
            models.Q(product__description__icontains=value)
        )

    class Meta:
        model = ProductVariant
        fields = []

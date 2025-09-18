import django_filters
from django.db import models
from shop.models import ProductVariant

class ProductVariantFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='product__brand__id')
    product_category = django_filters.CharFilter(field_name='product__product_category__id')
    country = django_filters.CharFilter(field_name='product__country__id')
    attribute_category = django_filters.CharFilter(field_name='attributes__attribute_category__id')
    search = django_filters.CharFilter(method='filter_search')

    @staticmethod
    def filter_search(queryset, name, value):
        return queryset.filter(
            models.Q(product__title__icontains=value) |
            models.Q(product__description__icontains=value)
        )

    class Meta:
        model = ProductVariant
        fields = []

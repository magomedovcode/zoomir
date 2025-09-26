from drf_spectacular.types import OpenApiTypes
from shop.models import Cart
from rest_framework import serializers
from shop.serializers.cart_content.product_in_cart_serializer import ProductInCartSerializer
from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema_field
)


@extend_schema_serializer(component_name='Cart')
class CartSerializer(serializers.ModelSerializer):
    products_in_cart = ProductInCartSerializer(
        many=True,
        read_only=True
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    total_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'date',
            'total_items',
            'total_price',
            'products_in_cart'
        ]
        read_only_fields = fields

    @extend_schema_field(OpenApiTypes.FLOAT)
    def get_total_items(self, obj):
        return obj.total_items()

    @extend_schema_field(OpenApiTypes.INT)
    def get_total_price(self, obj):
        return obj.total_price()

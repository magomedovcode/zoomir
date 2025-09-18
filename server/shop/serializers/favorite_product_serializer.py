from shop.models import FavoriteProduct
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from .product_serializer import ProductSerializer


@extend_schema_serializer(component_name='FavoriteProduct')
class FavoriteProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(
        read_only=True
    )
    user = serializers.StringRelatedField(
        read_only=True
    )
    class Meta:
        model = FavoriteProduct
        fields = [
            'id',
            'user',
            'date',
            'product'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='FavoriteProductCreate')
class FavoriteProductCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = FavoriteProduct
        fields = [
            'user',
            'product'
        ]

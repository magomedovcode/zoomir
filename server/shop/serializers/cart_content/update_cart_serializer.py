from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_serializer, extend_schema_field
from rest_framework import serializers
from shop.models import ProductInCart


@extend_schema_serializer(component_name='UpdateCartItem')
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ['quantity']

    @extend_schema_field(OpenApiTypes.INT)
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество должно быть не менее 1")
        return value

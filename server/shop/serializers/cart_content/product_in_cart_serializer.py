from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.product_variant_serializer import ProductVariantListSerializer
from shop.models import (
    ProductInCart,
    Cart
)


@extend_schema_serializer(component_name='ProductInCart')
class ProductInCartSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantListSerializer(
        read_only=True
    )

    class Meta:
        model = ProductInCart
        fields = [
            'id',
            'product_variant',
            'quantity'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ProductInCartCreate')
class ProductInCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = [
            'product_variant',
            'quantity'
        ]

    def create(self, validated_data):
        cart, created = Cart.objects.get_or_create(user=validated_data['user'])
        validated_data['cart'] = cart

        product_in_cart, created = ProductInCart.objects.get_or_create(
            cart=cart,
            product_variant=validated_data['product_variant'],
            defaults={'quantity': validated_data['quantity']}
        )

        if not created:
            product_in_cart.quantity += validated_data['quantity']
            product_in_cart.save()

        return product_in_cart

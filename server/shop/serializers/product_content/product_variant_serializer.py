from drf_spectacular.types import OpenApiTypes
from shop.models import ProductVariant
from rest_framework import serializers
from shop.serializers.product_content.attribute_category_serializer import AttributesPerCategorySerializer
from shop.serializers.product_content.product_image_serializer import ProductImageSerializer
from drf_spectacular.utils import (
    extend_schema_serializer,
    extend_schema_field
)


@extend_schema_serializer(component_name='VariantInProduct')
class VariantInProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(
        many=True,
        read_only=True
    )
    attributes = AttributesPerCategorySerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "name",
            "price",
            "product_images",
            "attributes",
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ProductVariantList')
class ProductVariantListSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source="product.title", read_only=True)
    first_image = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = [
            "id",
            "product_title",
            "price",
            "first_image",
            "average_rating",
            "reviews_count",
        ]

    @extend_schema_field(OpenApiTypes.URI)
    def get_first_image(self, obj):
        first_image = obj.product_images.first()
        if first_image and first_image.image:
            return first_image.image.url
        return None

    @extend_schema_field(OpenApiTypes.FLOAT)
    def get_average_rating(self, obj):
        return obj.product.average_rating()

    @extend_schema_field(OpenApiTypes.INT)
    def get_reviews_count(self, obj):
        return obj.product.reviews_count()

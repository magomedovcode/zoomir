from shop.models import ProductVariant
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.attribute_serializer import AttributeSerializer
from shop.serializers.product_content.product_image_serializer import ProductImageSerializer


@extend_schema_serializer(component_name='VariantInProduct')
class VariantInProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(
        many=True,
        read_only=True
    )
    attributes = AttributeSerializer(
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
            "attributes"
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

    @staticmethod
    def get_first_image(obj):
        image = obj.product_images.first()
        return image.image.url if image else None

    @staticmethod
    def get_average_rating(self, obj):
        return obj.product.average_rating()

    @staticmethod
    def get_reviews_count(self, obj):
        return obj.product.reviews_count()

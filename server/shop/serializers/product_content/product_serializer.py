from shop.models import Product
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers.product_content.product_variant_serializer import VariantInProductSerializer
from shop.serializers.user_content.review_serializer import ReviewSerializer
from shop.serializers.product_filters.brand_serializer import BrandSerializer
from shop.serializers.product_filters.country_serializer import CountrySerializer
from shop.serializers.product_filters.product_category_serializer import ProductCategorySerializer
from shop.serializers.product_content.tag_serializer import TagSerializer


@extend_schema_serializer(component_name='Product')
class ProductSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(
        read_only=True
    )
    brand = BrandSerializer(
        read_only=True
    )
    country = CountrySerializer(
        read_only=True
    )
    tags = TagSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'country',
            'product_category',
            'brand',
            'tags'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ProductDetail')
class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name")
    country = serializers.CharField(source="country.name")
    product_category = serializers.CharField(source="product_category.name")
    product_variants = VariantInProductSerializer(
        many=True,
        read_only=True
    )
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )
    tags = TagSerializer(
        read_only=True,
        many=True
    )
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "brand",
            "country",
            "product_category",
            "product_variants",
            "reviews",
            "average_rating",
            "reviews_count",
            "tags"
        ]

    @staticmethod
    def get_average_rating(obj):
        return obj.average_rating()

    @staticmethod
    def get_reviews_count(self, obj):
        return obj.reviews_count()

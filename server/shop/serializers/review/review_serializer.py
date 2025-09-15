from shop.models import Review, ReviewPhoto
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from shop.serializers import ProductSerializer, ReviewPhotoSerializer
from django.utils.translation import gettext_lazy as _


@extend_schema_serializer(component_name='Review')
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True
    )
    product = ProductSerializer(
        read_only=True,
    )
    review_photos = ReviewPhotoSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'product',
            'title',
            'comment',
            'rating',
            'date',
            'review_photos'
        ]
        read_only_fields = fields


@extend_schema_serializer(component_name='ReviewCreate')
class ReviewCreateSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(
            allow_empty_file=False,
            use_url=False
        ),
        required=False,
        write_only=True,
        help_text=_('Список фотографий для отзыва')
    )
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Review
        fields = [
            'user',
            'product',
            'title',
            'rating',
            'comment',
            'photos'
        ]

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        review = Review.objects.create(**validated_data)

        for photo_data in photos_data:
            ReviewPhoto.objects.create(review=review, photo=photo_data)

        return review

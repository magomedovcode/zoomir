from nested_admin.nested import NestedTabularInline
from shop.models import (
    ConnectedTag,
    Attribute,
    ProductImage,
    ProductVariant,
    ReviewPhoto,
    ProductInOrder,
    ProductInCart
)


class ConnectedTagInline(NestedTabularInline):
    model = ConnectedTag
    extra = 1
    fields = ['tag']
    autocomplete_fields = ['tag']


class AttributeInline(NestedTabularInline):
    model = Attribute
    extra = 1
    fields = ['name', 'value', 'product_variant', 'attribute_category']
    autocomplete_fields = ['product_variant', 'attribute_category']


class ProductImageInline(NestedTabularInline):
    model = ProductImage
    extra = 1
    fields = ['product_variant', 'image']
    autocomplete_fields = ['product_variant']


class ProductVariantInline(NestedTabularInline):
    model = ProductVariant
    extra = 1
    fields = ['name', 'price']
    inlines = [AttributeInline, ProductImageInline, ConnectedTagInline]


class ReviewPhotoInline(NestedTabularInline):
    model = ReviewPhoto
    extra = 1
    fields = ['review', 'photo']
    autocomplete_fields = ['review']


class ProductInOrderInline(NestedTabularInline):
    model = ProductInOrder
    extra = 1
    fields = ['order', 'product_variant', 'price', 'quantity']
    autocomplete_fields = ['order', 'product_variant']


class ProductInCartInline(NestedTabularInline):
    model = ProductInCart
    extra = 1
    fields = ['cart', 'product_variant', 'quantity']
    autocomplete_fields = ['cart', 'product_variant']

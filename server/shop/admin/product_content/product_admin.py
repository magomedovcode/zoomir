from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.admin.inlines import ProductVariantInline
from shop.models import Product


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ('title', 'description', 'product_category', 'country', 'brand')
    list_filter = ('product_category', 'country', 'brand')
    search_fields = ('title', 'description')
    ordering = ['id']
    autocomplete_fields = ['product_category', 'country', 'brand']
    inlines = [ProductVariantInline]
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('product_category', 'country', 'brand')
        }),
        ('Заполните поля', {
            'fields': ('title', 'description'),
        }),
    )

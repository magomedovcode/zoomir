from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(NestedModelAdmin):
    list_display = ('name', 'product_chapter')
    list_filter = ('product_chapter', )
    search_fields = ('name', )
    ordering = ['name']
    autocomplete_fields = ['product_chapter']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('product_chapter', )
        }),
        ('Заполните поля', {
            'fields': ('name',),
        }),
    )

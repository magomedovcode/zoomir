from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import FavoriteProduct


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(NestedModelAdmin):
    list_display = ('user', 'product', 'date')
    list_filter = ('user', 'product', 'date')
    search_fields = ('user__username', 'product__title')
    ordering = ['-date']
    autocomplete_fields = ['user', 'product']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('user', 'product')
        }),
    )

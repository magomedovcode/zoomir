from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.admin.inlines import ProductInCartInline
from shop.models import Cart


@admin.register(Cart)
class CartAdmin(NestedModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user__username',)
    ordering = ['-date']
    autocomplete_fields = ['user']
    inlines = [ProductInCartInline]
    list_per_page = 20

    fieldsets = (
        ('Выберите пользователя', {
            'fields': ('user',),
        }),
    )

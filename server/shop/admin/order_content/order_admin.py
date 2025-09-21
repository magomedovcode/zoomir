from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.admin.inlines import ProductInOrderInline
from shop.models import Order


@admin.register(Order)
class OrderAdmin(NestedModelAdmin):
    list_display = ('id', 'user', 'address', 'phone', 'delivery_date', 'status')
    list_filter = ('status', 'delivery_date')
    search_fields = ('id', 'user__username', 'address', 'phone')
    autocomplete_fields = ['user']
    inlines = [ProductInOrderInline]
    readonly_fields = ('date',)
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('user', 'status')
        }),
        ('Заполните поля', {
            'fields': ('address', 'phone', 'delivery_date'),
        }),
    )
from django.contrib import admin
from nested_admin.nested import NestedModelAdmin
from shop.models import Review


@admin.register(Review)
class ReviewAdmin(NestedModelAdmin):
    list_display = ('user', 'product', 'title', 'rating', 'comment')
    list_filter = ('user', 'product')
    search_fields = ('title', 'rating', 'comment',)
    ordering = ['-date']
    autocomplete_fields = ['user', 'product']
    list_per_page = 20

    fieldsets = (
        ('Выберите параметры', {
            'fields': ('user', 'product')
        }),
        ('Заполните поля', {
            'fields': ('title', 'rating', 'comment'),
        }),
    )

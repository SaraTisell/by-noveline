from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'category',
        'image',
    )

    ordering = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

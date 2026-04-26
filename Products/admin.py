# products/admin.py
from django.contrib import admin
from .models import Products, Category, ProductLike

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category', 'color', 'created_at']
    list_filter = ['price', 'stock', 'category', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock']

@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'product__name']

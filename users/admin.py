from django.contrib import admin
from .models import  Category, Products, Purchase, Cart, UserProfile

admin.site.register(Purchase)

# @admin.register()

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

admin.site.register(UserProfile)
admin.site.site_header='Gagarian Adminstration'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
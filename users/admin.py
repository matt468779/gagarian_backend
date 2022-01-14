from django.contrib import admin
from .models import  Category, Packages, Products, Purchase, Cart, UserProfile

admin.site.register(Purchase)

# @admin.register()

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')

admin.site.register(UserProfile)
admin.site.site_header='Gagarian Adminstration'

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'minimum', 'maximum', 'discount')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
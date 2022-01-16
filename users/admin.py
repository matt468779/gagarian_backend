from django.contrib import admin
from .models import  Category, Package, PackageItems, Products, Purchase, Cart, UserProfile

admin.site.register(Purchase)

# @admin.register()

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')

admin.site.register(UserProfile)
admin.site.site_header='Gagarian Adminstration'

@admin.register(Package)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PackageItems)
class PackageItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'product', 'quantity')
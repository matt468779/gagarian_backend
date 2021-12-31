from django.contrib import admin
from .models import  Products, Purchase, Cart, UserProfile

admin.site.register(Products)
admin.site.register(Purchase)

# @admin.register()

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

admin.site.register(UserProfile)


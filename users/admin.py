from django.contrib import admin
from .models import  Products, Purchase, Cart, UserProfile

admin.site.register(Products)
admin.site.register(Purchase)
admin.site.register(Cart)
admin.site.register(UserProfile)


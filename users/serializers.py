from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Products, Purchase, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'available', 'price']

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    # id = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['products']
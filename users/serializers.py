from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Products, Purchase, Cart, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'available', 'price', 'image']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    # id = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['product', 'quantity']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user', 'image']
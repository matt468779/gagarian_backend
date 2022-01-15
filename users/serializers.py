from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import Category, Packages, Products, Purchase, Cart, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups', 'password']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Products
        fields = ['name', 'available', 'price', 'image', 'description', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Products
        fields = ['id', 'name', 'name_locale', 'slug', 'tag', 'available', 'price', 'image1', 'image2', 'image3', 'description', 'category']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    # id = UserSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user', 'image']

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['name', 'miinimum', 'maximum', 'discount', 'description']

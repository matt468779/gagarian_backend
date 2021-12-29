from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.slug

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.product.name

class Cart(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    products = models.ManyToManyField(Products)
     

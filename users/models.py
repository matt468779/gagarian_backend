from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/%Y/%m/%d', blank=True)
    homeLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    deliveryLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default='ordered')
    def __str__(self) -> str:
        return self.product.name

class Cart(models.Model):
    class Meta:
        unique_together = (('user', 'product'))

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.product) + " " + str(self.quantity)


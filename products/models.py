#Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    productCode = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    profilePicture = models.ImageField(default="avatar1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    orderCode = models.CharField(max_length=50, null=True)
    orderdate = models.DateTimeField(auto_now_add=True, null=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.orderCode
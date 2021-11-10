# from typing import cast
from django.db import models
# from django.contrib.auth import get_user_model
# from django.db.models.base import Model
# from django.db.models.deletion import CASCADE, PROTECT
from product.models import Product
# from django.db.models.fields.related import ForeignKey

# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(
        verbose_name=('Full Name'),
        max_length=128,
    )
    username = models.CharField(
        unique=True,
        verbose_name=('Username'),
        max_length=128,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name=('Profile Picture'),
        upload_to='uploads',
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        verbose_name=('Email'),
        max_length=256,
    )
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )
    address = models.TextField()

    def __str__(self):
        return self.full_name


class FavoriteList(models.Model):
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )
    owner = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        Product
    )

    def __str__(self):
        return f'{self.owner} Favorite List'

class Comment(models.Model):
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
        )
    on_product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )

    body = models.TextField()

    def __str__(self):
        return f'{self.owner} Comment'

class Order(models.Model):
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )
    buyer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(
        Product,
    )

    def __str__(self):
        return f'{self.buyer} Order'

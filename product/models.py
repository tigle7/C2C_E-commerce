from django.db import models
# from customer.models import Customer, Comment, Order

# Create your models here.


class Category(models.Model):

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    title = models.CharField(
        verbose_name=('Category Title'),
        max_length=255
    )
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )

    def __str__(self):
        return self.title


class Product(models.Model):

    title = models.CharField(
        verbose_name=('Title'),
        max_length=255
    )
    create_at = models.DateTimeField(
        verbose_name=('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=('Updated Time'),
        auto_now=True
    )
    image = models.ImageField(
        verbose_name=('Picture'),
        upload_to='uploads',
    )
    category = models.ManyToManyField(
        Category,
    )
    desc = models.TextField(
        verbose_name=('Description')
    )
    price = models.PositiveIntegerField(
        verbose_name=('Price')

    )

    def __str__(self):
        return self.title

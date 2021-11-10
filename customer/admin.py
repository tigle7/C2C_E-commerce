from django.contrib import admin
from .models import Comment, Customer, FavoriteList, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(FavoriteList)
admin.site.register(Order)
from django.contrib import admin
from .models import *

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'amount', 'poster', 'rating', 'description')
    list_filter = ('description'),
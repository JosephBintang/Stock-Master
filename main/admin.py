from django.contrib import admin
from .models import *

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name','amount', 'date_added', 'price')
    list_filter = ('date_added'),
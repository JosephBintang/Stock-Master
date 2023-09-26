from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    poster = models.URLField(max_length=255, null=True)
    rating = models.TextField(null=True)
    description = models.TextField()
from django.db import models
from shop.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

class Promotion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
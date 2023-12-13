from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)

class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()

from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_introdution = models.TextField()
    product_image = models.ImageField(blank=True, null=True)
    brand = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_name)
from django.db import models
from .base_models import BaseModel


class Product(BaseModel):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products-images/')

    def __str__(self):
        return self.name
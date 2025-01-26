from django.db import models
from products.base_models import BaseModel


class Category(BaseModel):
    description = models.TextField()
    icon = models.ImageField(upload_to='category-icons/')

    def __str__(self):
        return self.name
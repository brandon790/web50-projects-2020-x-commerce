from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    start_bid = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.title}"
    
    class Category(models.Model):
        FASHION = 'FAS'
        TOYS = 'TOY'
        ELECTRONICS = 'ELC'
        HOME = 'HOM'
        CATEGORY_CHOICES = [
            (FASHION, 'Fashion'),
            (TOYS, 'Toys'),
            (ELECTRONICS, 'Electronics'),
            (HOME, 'Home'),
        ]
        category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=HOME)
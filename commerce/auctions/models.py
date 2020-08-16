from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    pass



class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    start_bid = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(blank=True)
    cat_choice = (
        ('Fashion' , 'Fashion'),
        ('Toys' , 'Toys'),
        ('Electronics' ,'Electronics'),
        ('Home' ,'Home'),
    )
    category = models.CharField(max_length=12, choices=cat_choice, default='Home')
    def __str__(self):
        return f"{self.id}: {self.title}"
    
    
class Bid(models.Model):
    bids = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.bids}"

class Comment(models.Model):
    comments = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id}: {self.comments}"
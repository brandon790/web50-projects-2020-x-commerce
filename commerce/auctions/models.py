from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    pass


class Watchlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='watchlist')
    watchlist = models.IntegerField()

    def __str__(self):
        return f"{self.user}:{self.watchlist}"
        
class Listing(models.Model):
    active = models.BooleanField(default=True)
    cat_choice = (
        ('Fashion' , 'Fashion'),
        ('Toys' , 'Toys'),
        ('Electronics' ,'Electronics'),
        ('Home' ,'Home'))
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    start_bid = models.DecimalField(max_digits=4, decimal_places=2)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=12, choices=cat_choice, default='Home')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_by', default=0)
    def __str__(self):
        return f"{self.id}:{self.title}: {self.created_by}"


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    bid = models.IntegerField()
    bid_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bid_by')


    def __str__(self):
        return f"{self.listing}: {self.bid}"

        
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments', null=True)
    comment = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f"{self.listing}"
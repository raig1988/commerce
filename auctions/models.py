from typing_extensions import Required
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

active = 'Active'
closed = 'Closed'
status_choices = [
    (active, 'Active'),
    (closed, 'Closed'),
]

class User(AbstractUser):
    pass
# Already inherits from AbstractUser, fields like username, email, password, etc but you can add new fields if desired.

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.category}"

class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_price = models.FloatField(max_length=20)
    image = models.ImageField(upload_to='auctions/files/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    status = models.CharField(max_length=20, choices=status_choices, default=active)

    def __str__(self):
        return f"{self.title} - {self.start_price} - {self.category}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ManyToManyField(AuctionListing)

    def __str__(self):
        return f"{self.user} - Watchlist item {self.auction}"

class Comments(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} made {self.comment} on {self.listing}"

class BidPrice(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    last_bid = models.FloatField(max_length=20, blank=True, null=True)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} bid on {self.listing} : {self.last_bid}"


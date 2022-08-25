from django.contrib import admin
from .models import User, Category, AuctionListing, Comments, BidPrice, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Comments)
admin.site.register(BidPrice)
admin.site.register(Watchlist)

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import User, AuctionListing, Category, Watchlist, BidPrice, Comments
from .forms import AddComment, CreateListingForm, UpdateStatus


def index(request):
    return render(request, "auctions/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    form = CreateListingForm()
    if request.method == "POST":
        form = CreateListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_price = form.cleaned_data['start_price']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']
            chosen_category = Category.objects.filter(category=category).first()
            inputdata = AuctionListing(user=request.user, title=title, description=description, start_price=start_price, image=image, category=chosen_category)
            inputdata.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, "auctions/create_listing.html", { "form" : form })

def active_listings(request):
    return render(request, "auctions/active_listings.html", {"active_listings" : AuctionListing.objects.all()})

def closed_listings(request):
    return render(request, "auctions/closed_listings.html", {"closed_listings" : AuctionListing.objects.all(), "BidPrice" : BidPrice.objects.all()})

def listing(request, listing):
    selectedlisting = AuctionListing.objects.get(id=listing)
    listingComments = Comments.objects.filter(listing=selectedlisting).all()
    return render(request, "auctions/listing.html", {"listing" : selectedlisting, 
                        "form_status": UpdateStatus(), "form_comment": AddComment(), "comments" : listingComments})

def watchlist_add(request, listing):
    item = get_object_or_404(AuctionListing, pk=listing)
    if Watchlist.objects.filter(user=request.user, auction=listing).exists():
        watchlist = Watchlist.objects.get(user=request.user)
        item.watchlist_set.remove(watchlist)
        messages.add_message(request, messages.SUCCESS, "Item deleted from watchlist.")
        return HttpResponseRedirect(reverse("watchlist"))
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    user_list.auction.add(item)
    user_list.save()
    messages.add_message(request, messages.SUCCESS, "Added to your watchlist.")
    return HttpResponseRedirect(reverse("watchlist"))

def watchlist(request):
    watchlist = Watchlist.objects.get(user=request.user)
    select = watchlist.auction.all()
    return render(request, "auctions/watchlist.html", {"watchlist" : select })

def change_status(request, listing):
    form = UpdateStatus()
    item = AuctionListing.objects.get(id=listing)
    auth_user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = UpdateStatus(request.POST)
        if item.user == auth_user:
            if form.is_valid():
                change_status = form.cleaned_data["status"]
                item.status = change_status
                item.save()
                return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))
        else:
            messages.add_message(request, messages.SUCCESS, "You are not authorized")
            return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))
    return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))

def set_bid(request, listing):
    selectedlisting = AuctionListing.objects.get(id=listing)
    if request.method == "POST":
        last_bid = request.POST["last_bid"]
        update_bid = BidPrice(user=request.user, last_bid=last_bid, listing=selectedlisting)
        update_bid.save()
        selectedlisting.start_price = last_bid
        selectedlisting.save()
        return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))
    return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))

def add_comment(request, listing):
    selectedlisting = AuctionListing.objects.get(id=listing)
    form = AddComment()
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            addcomment = Comments(user=request.user, comment=comment, listing=selectedlisting)
            addcomment.save()
            return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))
    return HttpResponseRedirect(reverse('listing', kwargs={'listing' : listing}))

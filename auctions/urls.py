from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("active_listings", views.active_listings, name="active_listings"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("listing/<int:listing>", views.listing, name="listing"),
    path("watchlist_add/<int:listing>", views.watchlist_add, name="watchlist_add"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("change_status/<int:listing>", views.change_status, name="change_status"),
    path("set_bid/<int:listing>", views.set_bid, name="set_bid"),
    path("add_comment/<int:listing>", views.add_comment, name="add_comment")
]

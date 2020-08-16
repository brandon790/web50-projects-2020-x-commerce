from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("categories/fashion", views.fashion, name="fashion"),
    path("categories/toys", views.toys, name="toys"),
    path("categories/electronics", views.electronics, name="electronics"),
    path("categories/home", views.home, name="home"),
    path("watchlist", views.watchlist, name="watchlist")




]

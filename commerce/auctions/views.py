from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CreateListingForm

from .models import User, Listing, Bid, Comment


def index(request):
    listing = Listing.objects.all().values('title','description','start_bid', 'image_url','category')
    print(listing)
    return render(request, "auctions/index.html", {
        "listing": listing,
    })


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

def create(request):
    form = CreateListingForm(request.POST or None)
    if form.is_valid():
        form.save()
        title = request.POST.get('title')
        return HttpResponseRedirect((f"listing/{ title }"))

    return render(request, "auctions/create.html", {
        'create_listing': CreateListingForm })

def listing(request, title):
        current_title = Listing.objects.filter(title=title).values('title')
        for i in current_title:
            current_title = i['title']
        current_des = Listing.objects.filter(title=title).values('description')
        for i in current_des:
            current_des = i['description']
        current_stbid = Listing.objects.filter(title=title).values('start_bid')
        for i in current_stbid:
            current_stbid = i['start_bid']
        current_imgurl = Listing.objects.filter(title=title).values('image_url')
        for i in current_imgurl:
            current_imgurl = i['image_url']
        current_cat = Listing.objects.filter(title=title).values('category')
        for i in current_cat:
            current_cat = i['category']
            

        return render(request, "auctions/listing.html", {
            "title": current_title,
            "description": current_des,
            "start_bid": current_stbid,
            "img_url" : current_imgurl,
            "cat": current_cat
        })

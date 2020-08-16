from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CreateListingForm
from django.contrib.auth.decorators import login_required


from .models import User, Listing, Bid, Comment, Watchlist


def index(request):
    listing = Listing.objects.all().values('title','description','start_bid', 'image_url','category')
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
    ##will get the specific bids on the listing
    ##current_bids =(Bid.objects.filter(listing__title=title)).values('bid')

    current_id = Listing.objects.filter(title=title).values('id')
    for i in current_id:
        current_id = i['id']
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
    
    watchlist = (Watchlist.objects.filter(user__username=request.user))
    users_watchlist = []
    for i in watchlist:
        users_watchlist.append(i.watchlist)
    add_watch = None
    if current_id in users_watchlist:
        add_watch = True
    else:
        add_watch = False

    if request.method == "POST":
        if request.POST.get('addwatch') == 'yes':
            c = Watchlist(user=request.user, watchlist=current_id)
            c.save()
            return HttpResponseRedirect((f"{ title }"))
        elif request.POST.get('removewatch') == 'yes':
            c = Watchlist.objects.filter(watchlist=current_id)
            c.delete()
            return HttpResponseRedirect((f"{ title }"))



    return render(request, "auctions/listing.html", {
        "title": current_title,
        "description": current_des,
        "start_bid": current_stbid,
        "img_url" : current_imgurl,
        "cat": current_cat,
        "add_watch": add_watch
        })
    




def categories(request):
    return render(request, "auctions/categories.html")

def fashion(request):
    listing = Listing.objects.filter(category='Fashion')
    return render(request, "auctions/fashion.html", {
            "listing": listing,
    })   

def toys(request):
    listing = Listing.objects.filter(category='Toys')
    return render(request, "auctions/toys.html", {
            "listing": listing,
    })    

def electronics(request):
    listing = Listing.objects.filter(category='Electronics')
    return render(request, "auctions/electronics.html", {
            "listing": listing,
    })
def home(request):
    listing = Listing.objects.filter(category='Home')
    return render(request, "auctions/home.html", {
            "listing": listing,
    })

def watchlist(request):
    watchlist = (Watchlist.objects.filter(user__username=request.user))
    users_watchlist = []
    for i in watchlist:
        users_watchlist.append(i.watchlist)

    listing = Listing.objects.filter(id__in=users_watchlist)
    return render(request, "auctions/watchlist.html", {
        "listing": listing,
    })
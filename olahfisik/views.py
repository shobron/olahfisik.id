from django.shortcuts import render
from olahfisik.models import *

# Create your views here.
def index_view(request):
    return render(request, 'olahfisik/index.html')

def categories_view(request):
    return render(request, 'olahfisik/categories.html')

def lari_view(request):
    venues = Venue.objects.filter(type=1)
    return render(request, 'olahfisik/lari.html', {'venues' : venues})

def bad_view(request):
    venues = Venue.objects.filter(type=2)
    return render(request, 'olahfisik/bad.html', {'venues' : venues})

def fut_view(request):
    venues = Venue.objects.filter(type=3)
    return render(request, 'olahfisik/fut.html', {'venues' : venues})

def ren_view(request):
    venues = Venue.objects.filter(type=4)
    return render(request, 'olahfisik/ren.html', {'venues' : venues})

def sen_view(request):
    venues = Venue.objects.filter(type=5)
    return render(request, 'olahfisik/sen.html', {'venues' : venues})

def ping_view(request):
    venues = Venue.objects.filter(type=6)
    return render(request, 'olahfisik/ping.html', {'venues' : venues})

def details_view(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'olahfisik/details.html', {'venue' : venue})

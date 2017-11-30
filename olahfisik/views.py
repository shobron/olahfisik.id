from django.shortcuts import render
from olahfisik.models import *

# Create your views here.
def index_view(request):
    return render(request, 'olahfisik/index.html')

def categories_view(request):
    return render(request, 'olahfisik/categories.html')

def results_view(request):
    venues = Venue.objects.all()
    return render(request, 'olahfisik/results.html', {'venues' : venues})

def details_view(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    x = 0
    return render(request, 'olahfisik/details.html', {'venue' : venue}, {'x':x})

from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'olahfisik/index.html')

def categories_view(request):
    return render(request, 'olahfisik/categories.html')

def results_view(request):
    return render(request, 'olahfisik/results.html')

def details_view(request):
    return render(request, 'olahraga/details.html')

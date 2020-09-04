from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'search/home.html')

def about(request):
    return render(request, 'search/about.html')

def classes(request):
    return render(request, 'search/classes.html')

def register(request):
    return render(request, 'user/register.html')
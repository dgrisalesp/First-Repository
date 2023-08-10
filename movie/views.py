from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def home (request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm=request.GET.get('searchMovie')
    return render (request,'home.html',{'searchTerm':searchTerm})
def About(request):
    return render (request,"About.html",{'name':"David Grisales Posada"})

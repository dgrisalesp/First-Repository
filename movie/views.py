from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def home (request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    searchTerm=request.GET.get('searchMovie')
    movies=Movie.objects.all()
    return render (request,'movie/home.html',{'searchTerm':searchTerm,'movies':movies})
def About(request):
    return render (request,"movie/About.html",{'name':"David Grisales Posada"})

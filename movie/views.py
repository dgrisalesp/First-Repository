from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    return render (request,'home.html',{'name':'David Grisales Posada'})
def About(request):
    return render (request,"About.html",{'name':"David Grisales Posada"})

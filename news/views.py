from django.shortcuts import render
from . import models
# Create your views here.
def news(request):
    newss=models.News.objects.all().order_by('-date')
    return render(request,'news/news.html',{'newss':newss})
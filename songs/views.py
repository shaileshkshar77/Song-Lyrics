from django.shortcuts import render
from .models import Songs
from django.http import HttpResponse

def list(request):
    articles=Songs.objects.all()
    return render(request ,"songs/list.html",{"articles":articles})

def article(request,slug):
    #return HttpResponse(slug)
    song=Songs.objects.get(slug=slug)
    return render(request ,"songs/lyric.html",{"song":song})

# Create your views here.

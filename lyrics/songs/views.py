from django.shortcuts import render
from .models import Songs

def list(request):
    articles=Songs.objects.all()
    return render(request ,"songs/list.html",{"articles":articles})

# Create your views here.

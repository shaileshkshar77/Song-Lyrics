from django.shortcuts import render

def list(request):
    return render(request ,"songs/list.html")

# Create your views here.

from django.shortcuts import render,redirect
from .models import Songs
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def list(request):
    articles=Songs.objects.all()
    return render(request ,"songs/list.html",{"articles":articles})

def article(request,slug):
    #return HttpResponse(slug)
    song=Songs.objects.get(slug=slug)
    return render(request ,"songs/lyric.html",{"song":song})

@login_required(login_url="/accounts/login/")
def create_song(request):
    if request.method =='POST':
        form=forms.CreateSongs(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('song:good')
    else:
        form =forms.CreateSongs()
    return render(request,"songs/create.html",{'form':form})

# Create your views here.

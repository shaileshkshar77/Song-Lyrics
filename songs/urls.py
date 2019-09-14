from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='song'

urlpatterns = [
    
    path('',views.list,name="good"),
    path('create/',views.create_song,name="create"),
    re_path('(?P<slug>[\w-]+)/$',views.article,name="detail"),
]

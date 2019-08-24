from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    
    path('',views.list),
    path('(<slug:slug>/',views.article),
]

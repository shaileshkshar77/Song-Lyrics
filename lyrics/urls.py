from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from songs import views as song_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/',include('songs.urls')),
    path('accounts/',include('accounts.urls')),
    path('about/',views.about),
    path('',song_views.list,name='home'),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



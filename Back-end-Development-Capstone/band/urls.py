from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='home'),path('concerts/',views.concerts,name='concerts'),path('songs/',views.songs,name='songs'),path('photos/',views.photos,name='photos')]

import requests
from django.conf import settings
from django.shortcuts import render
from .models import Concert

def _json(url, fallback):
 try:
  r=requests.get(url,timeout=2); r.raise_for_status(); return r.json()
 except Exception: return fallback

def home(request): return render(request,'home.html')
def concerts(request): return render(request,'concerts.html',{'concerts':Concert.objects.order_by('date')})
def songs(request): return render(request,'songs.html',{'songs':_json(settings.SONGS_URL+'/song',[])})
def photos(request): return render(request,'photos.html',{'photos':_json(settings.PICTURES_URL+'/picture',[])})

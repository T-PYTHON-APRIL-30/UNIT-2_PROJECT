from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_page(request :HttpRequest):

    return render(request,"personal_app/home.html")

def gallery_page(request :HttpRequest):

    return render(request,"personal_app/gallery.html")

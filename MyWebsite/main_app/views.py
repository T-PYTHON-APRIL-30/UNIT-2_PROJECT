from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.
def home_page(request: HttpRequest):
    return render(request, 'main_app/home.html')


def about_page(request: HttpRequest):
    return render(request, 'main_app/about.html')


def projects_page(request: HttpRequest):
    return render(request, 'main_app/project.html')


def contact_page(request: HttpRequest):
    return render(request, 'main_app/contact.html')

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.


def test_page(request: HttpRequest):
    return render(request, "main_app/concat_me.html")

def home_page(request: HttpRequest):
    return render(request, "main_app/index.html")
def contact_me(request: HttpRequest):
    return render(request, "main_app/concat_me.html")
def blogs(request: HttpRequest):
    return render(request, "main_app/blogs.html")
def read_blogs(request: HttpRequest):
    return render(request, "main_app/read_blog.html")
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_page(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/personal.html")

def blog_page2(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/blog2.html")

def contact_me(request:HttpRequest):

    return render(request, "main_app/contect_me.html")


def blog_page(request:HttpRequest):


    return render(request, "main_app/blog.html")
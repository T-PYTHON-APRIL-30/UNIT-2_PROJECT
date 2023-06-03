from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def index_page(request:HttpRequest):

    return render(request,"profile_app/index.html")

def about_page(request:HttpRequest):

    return render(request,"profile_app/about.html")

def skill_page(request:HttpRequest):

    return render(request,"profile_app/skills.html")

def contact_page(request:HttpRequest):

    return render(request,"profile_app/contact.html")

def project_page(request:HttpRequest):

    return render(request,"profile_app/project.html")
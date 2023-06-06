from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import contact , Project

# Create your views here.

def home_page(request :HttpRequest):
    projects = Project.objects.all()

    return render(request,"personal_app/home.html",{"projects": projects})

def gallery_page(request :HttpRequest):

    return render(request,"personal_app/gallery.html")

def add_contact(request:HttpRequest):

    if request.method == "POST":
        new_contact = contact( name = request.POST["name"],email = request.POST["email"], message = request.POST["message"])
        new_contact.save()
        return redirect("personal_app:home_page")
    return render (request,"personal_app/home.html" )

def read_contact(request:HttpRequest):
    
        contacts = contact.objects.all()
        return render(request, 'personal_app/message.html', {"contacts": contacts})

def add_project(request:HttpRequest):
    if request.method == "POST":
        #addin a new blog in database
        new_project = Project(title=request.POST["title"], content=request.POST["content"], date=request.POST["date"], image=request.FILES["image"])
        new_project.save()
        return redirect("personal_app:home_page")

    return render(request,"personal_app/add_project.html" )

def project_details(request :HttpRequest, project_id):
    project = Project.objects.get(id=project_id)

    return render(request,"personal_app/project_details.html",{'project':project})

def delete_project(request:HttpRequest,project_id):
    project = Project.objects.get(id = project_id)
    project.delete()

    return redirect("personal_app:home_page")

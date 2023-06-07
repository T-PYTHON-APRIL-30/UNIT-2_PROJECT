from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact, Project
from datetime import datetime
from django.utils import timezone
# Create your views here.

def home_page(request:HttpRequest):
    project_object = Project.objects.all().order_by('project_date')
    return render(request, "main_app/home_page.html",{'projects': project_object})

#Project pages
def add_project(request:HttpRequest):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image=request.FILES['image']
        project_date = request.POST['project_date']
        project_object = Project.objects.create(title=title, description=description, project_date=project_date, image=image)
        project_object.save()
        return redirect('main_app:home_page')
    else:
        return render(request, "main_app/add_project.html")

def delete_project(request:HttpRequest, project_id):
    project= Project.objects.get(id= project_id)
    project.delete()
    return redirect("main_app:home_page")


def project_detail(request:HttpRequest,project_id):
    project = Project.objects.get(id = project_id)
    return render(request, "main_app/project_detail.html",{"projects":project})

#Contact pages

def add_message(request:HttpRequest):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        content= request.POST['content']
        subject=request.POST['subject']
        contact = Contact.objects.create(name=name, email=email, content=content, subject=subject)
        contact.save()
        return redirect('main_app:home_page')
    
    return render(request, "main_app/home_page.html") 
    
def read_message(request:HttpRequest):
    contact= Contact.objects.all()
    return render(request,"main_app/read_message.html",{"contacts":contact})


#games section
def game_one(request:HttpRequest):
    return render(request,"main_app/game_one.html")

def game_two(request:HttpRequest):
    return render(request,"main_app/game_two.html")

def game_three(request:HttpRequest):
    return render(request,"main_app/game_three.html")

def about_me(request:HttpRequest):
    return render(request,"main_app/about_me.html")
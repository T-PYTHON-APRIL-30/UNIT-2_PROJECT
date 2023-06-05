from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Project

# Create your views here.
def add_page(request: HttpRequest):
    if request.method == "POST":
        new_element = Project(
            title_project = request.POST["title_project"],
            description_project = request.POST["description_project"],
            ison_project = request.POST["ison_project"],
            image_project = request.FILES["image_project"]
        )
        new_element.save()

    return render(request, 'main_app/add_element.html')


def update_page(request: HttpRequest, project_id):
    project = Project.objects.get(id = project_id)
    if request.method == "POST":
        project.title_project = request.POST["title_project"]
        project.description_project = request.POST["description_project"]
        project.ison_project = request.POST["ison_project"]
        project.image_project = request.FILES["image_project"]
        project.save()

    return render(request, 'main_app/update_element.html', {"project" : project})


def home_page(request: HttpRequest):
    project = Project.objects.all()

    return render(request, 'main_app/home.html', {"project" : project})


def about_page(request: HttpRequest):
    return render(request, 'main_app/about.html')


def projects_page(request: HttpRequest):
    project = Project.objects.all()

    return render(request, 'main_app/project.html', {"project" : project})


def contact_page(request: HttpRequest):
    return render(request, 'main_app/contact.html')


def projects_detial_page(request: HttpRequest, project_id):
    project = Project.objects.get(id = project_id)

    return render(request, 'main_app/project_detial.html', {"project" : project})

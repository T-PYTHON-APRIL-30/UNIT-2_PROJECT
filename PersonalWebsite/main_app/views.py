from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Contact

# Create your views here.

def home(request:HttpRequest):


    return render(request, 'main_app/home.html')

def contact(request:HttpRequest):

    if request.method == "POST":
        new_contact = Contact(name = request.POST['name'], mail = request.POST['mail'], message = request.POST['message'])
        new_contact.save()
        return redirect("main_app:contact")

    return render(request, 'main_app/contact.html')

def about(request:HttpRequest):


    return render(request, 'main_app/about.html')

def courses(request:HttpRequest):


    return render(request, 'main_app/courses.html')

def contactor(request:HttpRequest, contactor_id):

    try:
        contactors = Contact.objects.get(id = contactor_id)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/contactor.html', {"contactors": contactors})


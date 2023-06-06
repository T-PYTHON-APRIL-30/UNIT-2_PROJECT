from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def resume(request):
    return render(request, 'myapp/resume.html')

def add_contact(request:HttpRequest):
    if request.method == 'POST':
        Cname = request.POST['name']
        Cemail = request.POST['email']
        Cmessage = request.POST['message']
        new_contact = Contact(name=Cname,email=Cemail,message=Cmessage)
        new_contact.save()
        context = "message sent successfully"
        return render(request, 'myapp/contact.html', {"msg":context})
    return render(request, 'myapp/contact.html')

def projects(request):
    return render(request, 'myapp/projects.html')

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

def add_review(request:HttpRequest):
    if request.method == 'POST':
        Rmessage = request.POST['message']
        Rdate = request.POST["created_at"]
        new_review = Review(message=Rmessage, created_at=Rdate)
        new_review.save()
        context = "review added successfully"
        return render(request, 'myapp/contact.html', {"msg":context})
    return render(request, 'myapp/contact.html')

def show_review(request):
    reviews = Review.objects()
    return render(request, 'mmyapp/contact.html', {'reviews': reviews})

def projects(request):
    return render(request, 'myapp/projects.html')

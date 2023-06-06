from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import ContactMe,Comment
# Create your views here.
def about_page(request:HttpRequest):
    return render(request,"about.html")

def myproject_page(request:HttpRequest):
    return render(request,'myproject.html')

def skill_page(request:HttpRequest):
    return render(request,'skill.html')

def contact_page(request:HttpRequest):
    comments=Comment.objects.all()
    return render(request,"contact.html", {"comments":comments})

def addComment(request:HttpRequest):
    if request.method=="POST":
        new_comment=Comment(name=request.POST["name"],content=request.POST["message"])
        new_comment.save()
        return redirect("my_app:contact_page")
def sendContact(request:HttpRequest):
    if request.method=="POST":
        new_send=ContactMe(name=request.POST["name"],email=request.POST["email"], message=request.POST["message"])
        new_send.save()
        return redirect("my_app:contact_page")



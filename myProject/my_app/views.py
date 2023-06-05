from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def about_page(request:HttpRequest):
    return render(request,"about.html")

def myproject_page(request:HttpRequest):
    return render(request,'myproject.html')

def skill_page(request:HttpRequest):
    return render(request,'skill.html')

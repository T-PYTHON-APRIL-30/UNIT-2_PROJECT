from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def resume(request):
    return render(request, 'myapp/resume.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def projects(request):
    return render(request, 'myapp/projects.html')

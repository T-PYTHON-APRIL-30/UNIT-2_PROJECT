from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Project, CvFile, Education, Experience, Skills, Courses
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home_page(request: HttpRequest):
    project = Project.objects.all()
    cv = CvFile.objects.all()

    return render(request, 'main_app/home.html', {"project" : project, "cv" : cv})


def about_page(request: HttpRequest):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills7 = Skills.objects.all()[:6]
    skills = Skills.objects.all()[6:]
    courses = Courses.objects.all()

    return render(request, 'main_app/about.html', {"education" : education, "experience" : experience, "skills7" : skills7, "skills" : skills, "courses" : courses})


def projects_page(request: HttpRequest):
    project = Project.objects.all()

    return render(request, 'main_app/project.html', {"project" : project})


def contact_page(request: HttpRequest):
    if request.method == "POST":
        message = request.POST['message']
        address = request.POST['address']
        name_first = request.POST['name_first']
        name_last = request.POST['name_last']
        subject = request.POST['subject']

        msg = f"From {name_first} {name_last},\n email: {address}\n\n{message}"

        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            ['alsaadan2000@gmail.com'],
            fail_silently=False)
        
        return redirect('main_app:thanks_page')

    return render(request, 'main_app/home.html')


def projects_detial_page(request: HttpRequest, project_id):
    project = Project.objects.get(id = project_id)

    return render(request, 'main_app/project_detial.html', {"project" : project})


def thanks_page(request: HttpRequest):
    return render(request, 'main_app/thanks.html')

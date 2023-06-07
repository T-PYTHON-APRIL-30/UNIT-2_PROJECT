from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Movies_TV, Career
from django.conf import settings
from django.core.mail import send_mail


def home(request: HttpRequest):
    return render(request, "main_app/home.html")


def contact_me(request: HttpRequest):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        subject = "Message From My Personal Website"
        messages = f"Name {name}, Email:{email}, Message: {message}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            "mk.97@outlook.sa",
        ]
        send_mail(subject, messages, email_from, recipient_list)
    return render(request, "main_app/contact_me.html")


def career(request: HttpRequest):
    careers = Career.objects.all
    return render(request, "main_app/career.html", {"careers": careers})


def interests(request: HttpRequest):
    movies_tv = Movies_TV.objects.all
    return render(request, "main_app/interests.html", {"movies_tv": movies_tv})

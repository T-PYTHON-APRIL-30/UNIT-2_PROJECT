from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Contact
# Create your views here.


def index_page(request: HttpRequest):

    return render(request, "profile_app/index.html")


def about_page(request: HttpRequest):

    return render(request, "profile_app/about.html")


def skill_page(request: HttpRequest):

    return render(request, "profile_app/skills.html")


def contact_page(request: HttpRequest):

    if request.method == "POST":
        new_contact = Contact(first_name=request.POST["first_name"], last_name=request.POST["last_name"],
                              email=request.POST["email"], mobile=request.POST["mobile"], message=request.POST["message"])
        new_contact.save()
        mg_successful = True
        return render(request, "profile_app/contact.html", {'msg_successful': mg_successful})

    return render(request, "profile_app/contact.html")


def project_page(request: HttpRequest):

    return render(request, "profile_app/project.html")


def message_cards(request: HttpRequest):
    all_msg = Contact.objects.all()

    return render(request, "profile_app/cards.html", {'messages': all_msg})

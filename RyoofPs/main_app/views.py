from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
from django.core.mail import send_mail


# Create your views here.

def index_page(request:HttpRequest):

    return render(request, "main_app/index.html") 



def about_me(request:HttpRequest):

    return render(request, "main_app/about-me.html") 



def services(request:HttpRequest):

    return render(request, "main_app/services.html") 


def portfolio(request:HttpRequest):

    return render(request, "main_app/portfolio.html") 



def contact(request:HttpRequest):
    if request.method == "POST":
        
        newContact = Contact(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
        newContact.save()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')
        
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message= '''
        New message:{}

        From: {}
        '''.format(form_data["message"], form_data["email"])
        send_mail(form_data["subject"],message,'ryuof-21_@hotmail.com',['ryuofalarfaj@gmail.com'])

        return redirect("main_app:submit_done")
    return render(request, "main_app/contact.html") 

def submit_done(request:HttpRequest):

    return render(request,"main_app/submit_done.html")
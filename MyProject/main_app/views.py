from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Subject, Contact
from django.core.mail import send_mail

# Create your views here.

def homePage(request:HttpRequest):

    subjects = Subject.objects.order_by('title')

    if request.method == "POST":
        newContact = Contact(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
        newContact.save()

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email': email,
            'subject' : subject,
            'message': message
        }

        message = '''
            new message: {}
            From: {}'''.format(data["message"], data["email"])
        send_mail(data["subject"],message,'amanii1994@outlook.com',['amanii1994@outlook.com'])




        return redirect("main_app:homePage")

    return render(request, "main_app/home.html", {"subjects" : subjects})


def newSubPage (request:HttpRequest):
    if request.method == "POST":
            
        newSub= Subject(title=request.POST["title"],author=request.POST["author"],heading1=request.POST["heading1"] ,articl1=request.POST["articl1"],heading2=request.POST["heading2"] ,articl2=request.POST["articl2"] ,publish_date=request.POST["publish_date"],main_image=request.FILES["main_image"],article_image1=request.FILES["article_image1"],article_image2=request.FILES["article_image2"] )
        newSub.save()

        return redirect("main_app:homePage")
    
    return render (request, "main_app/new_subject.html")

def detailsPage(request:HttpRequest, sub_id):

    sub = Subject.objects.get(id=sub_id)

    return render (request, "main_app/details.html", {'sub':sub})


def deleteSub(request:HttpRequest, sub_id):
    
    sub = Subject.objects.get(id=sub_id)
    sub.delete()

    return redirect("main_app:homePage")


def contactUs (request:HttpRequest):
    if request.method == 'POST':
        newContact= Subject(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
        newContact.save()

        return redirect("main_app:homePage")
    
    return render (request, "main_app/new_subject.html")


def searchPage(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    subjects = Subject.objects.filter(title__contains=search_phrase)

    return render(request, "main_app/search.html", {"subjects" : subjects})
    



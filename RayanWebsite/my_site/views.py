from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import message

# Create your views here.

def home_page(request:HttpRequest):

    return render(request, "my_site/home_page.html")

def about(request:HttpRequest):

    return render(request, "my_site/about.html")

def interests(request:HttpRequest):

    return render(request, "my_site/interests.html")

def skills(request:HttpRequest):

    return render(request, "my_site/skills.html")

def contact(request:HttpRequest):
    if request.method == "POST":
        new_message = message(name=request.POST["name"], email=request.POST["email"], title=request.POST["title"], content=request.POST["content"])
        new_message.save()


    return render(request, "my_site/contact.html")

def feedback(request:HttpRequest):

    comment = message.objects.all()
    
    return render(request, "my_site/feedback.html", {"comment":comment})

def delete(request:HttpRequest, comment_id):

    comment_d = message.objects.get(id=comment_id)
    comment_d.delete()

    return redirect("my_site:feedback_page")
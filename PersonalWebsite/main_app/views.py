from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post, Contact

# Create your views here.



def blog_page(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "main_app/blog_page.html", {"posts" : posts})

def testing_page(request: HttpRequest):
    return render(request, "main_app/testing_page.html")

def add_post(request:HttpRequest):

    if request.method == "POST":

        new_post = Post(title=request.POST["title"], content=request.POST["content"],
                         is_published=request.POST["is_published"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_post.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_post.html")



def index_page(request:HttpRequest):

    posts = Post.objects.all()

    return render(request, "main_app/index_page.html", {"posts" : posts})

def detail_page(request:HttpRequest, post_id):

    post = Post.objects.get(id=post_id)

    return render(request, 'main_app/detail_page.html', {"post" : post})

def contact_page(request: HttpRequest):
    if request.method == "POST":

        new_message = Contact(name=request.POST["name"], email=request.POST["email"],
                         subject=request.POST["subject"], message=request.POST["message"],)
        new_message.save()
        return redirect("main_app:index_page")
    return render(request, "main_app/contact_page.html")

def about_page(request: HttpRequest):
    return render(request, "main_app/about_page.html")

def projects_page(request: HttpRequest):
    return render(request, "main_app/projects_page.html")
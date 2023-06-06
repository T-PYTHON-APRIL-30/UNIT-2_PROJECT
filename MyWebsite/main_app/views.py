from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Review

# Create your views here.

def add_blog(request:HttpRequest):

    if request.method == "POST":
        #addin a new game in database
        new_blog = Blog(title=request.POST["title"], description=request.POST["description"], rating=request.POST["rating"], release_date=request.POST["release_date"], is_published=request.POST["is_published"], image=request.FILES["image"])
        new_blog.save()
        return redirect("main_app:index_page")

    return render(request, "main_app/add_blog.html")


def index_page(request:HttpRequest):
    

    blogs = Blog.objects.all()

    return render(request, "main_app/index.html", {"blogs" : blogs})

def blog_detail(request:HttpRequest, blog_id):

    try:
        blog = Blog.objects.get(id=blog_id)
        comments = Review.objects.filter(blog=blog)
    except:
        return render(request, 'main_app/not_found.html')

    return render(request, 'main_app/blog_detail.html', {"blog" : blog, "comments" : comments})


def update_blog(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    iso_date = blog.release_date.isoformat()


    #updating the blog
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.description = request.POST["description"]
        blog.rating = request.POST["rating"]
        blog.release_date = request.POST["release_date"]
        blog.is_published = request.POST["is_published"]

        if "image" in request.FILES:
            blog.image = request.FILES["image"]
        blog.save()

        return redirect("main_app:blog_detail", blog_id=blog.id)

    return render(request, 'main_app/update_blog.html', {"blog" : blog, "iso_date" : iso_date})




def delete_game(request:HttpRequest, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("main_app:index_page")

def add_review(request:HttpRequest, blog_id):

    if request.method == "POST":
        blog_object = Blog.objects.get(id=blog_id)
        new_review = Review(blog=blog_object, name=request.POST["name"], content=request.POST["content"])
        new_review.save()
    
    return redirect("main_app:blog_detail", blog_id=blog_id)

def perosnal_page(request: HttpRequest):
    #to use template , we use render and pass in the path to the template
    return render(request, "main_app/personal.html")
    

def contact_me(request:HttpRequest):

    return render(request, "main_app/contect_me.html")

def about_me(request:HttpRequest):

    return render(request, "main_app/about_me.html")
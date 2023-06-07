from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post, Review

# Create your views here.
def home_page(request:HttpRequest ):
    return render (request, "main_app/home.html")
def about_page(request:HttpRequest ):
    return render (request, "main_app/about.html")
def contact_page(request:HttpRequest ):
    return render (request, "main_app/contact.html")
def soon_page(request:HttpRequest ):
    return render (request, "main_app/soon.html")
# For Add Photo
def add_painting(request:HttpRequest ):
    if request.method == "POST":
            view_post = Post(title=request.POST["title"], description=request.POST["description"], date=request.POST["date"], size=request.POST["size"] , price=request.POST["price"] , img = request.FILES["img"],hour = request.POST["hour"],rating = request.POST["rating"], type=request.POST["type"])
            view_post.save() 
            if request.POST["type"] == "Manual":
                return redirect("main_app:manual")
            elif request.POST["type"] == "Digital":
                return redirect("main_app:digital")
            elif request.POST["type"] == "Web":
                return redirect("main_app:web_design")
    return render (request, "main_app/Add_painting.html")
#For review
def add_review(request:HttpRequest, post_id):
    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        new_review = Review(post=post_object, name=request.POST["name"], content=request.POST["content"], rating=request.POST["rating"])
        new_review.save()
    return redirect("main_app:comments", post_id=post_id)
# For add comments
def comments(request:HttpRequest, post_id):
    try:
        post_detail1 = Post.objects.get(id = post_id)
        comments1 = Review.objects.filter(post=post_detail1)
    except:
         return render(request, 'main_app/not_found.html')
    return render (request,"main_app/comments.html",{"post_detail1" : post_detail1, "comments1" : comments1})
#For update post
def update_post(request:HttpRequest,post_id):
    update_detail1 = Post.objects.get(id = post_id)
    iso_date = update_detail1.date.isoformat()
    if request.method == "POST":
            update_detail1.title=request.POST["title"]
            update_detail1.description = request.POST["description"]
            update_detail1.date = request.POST["date"]
            update_detail1.size = request.POST["size"]
            update_detail1.price = request.POST["price"]
            update_detail1.hour = request.POST["hour"]
            if "img" in request.FILES : 
                update_detail1.img = request.FILES["img"]
            update_detail1.save()
            return redirect("main_app:comments", post_id = update_detail1.id)
    return render (request,"main_app/update.html",{"update_detail1" : update_detail1,"iso_date" : iso_date})
#For delete post
def delete_post(request:HttpRequest, post_id):
    delete_detail1 = Post.objects.get(id = post_id)
    delete_detail1.delete()
    return redirect("main_app:home_page")
#For view objects
def manual(request:HttpRequest ):
    view_post = Post.objects.filter(type="Manual")
    return render (request, "main_app/paintings.html", {"view_post" : view_post})
def digital(request:HttpRequest ):
    view_post = Post.objects.filter(type="Digital")
    return render (request, "main_app/paintings.html",{"view_post" : view_post})

def web_design(request:HttpRequest ):
    view_post = Post.objects.filter(type="Web")
    return render (request, "main_app/paintings.html", {"view_post" : view_post})
def update(request:HttpRequest ):
    return render (request, "main_app/update.html")
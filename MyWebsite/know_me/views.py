from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Course

# Create your views here.

# Home Page
def home_page(request:HttpRequest):
    return render(request,"know_me/home_page.html")

# Gallery Page
def gallery_page(request:HttpRequest):
    return render(request,"know_me/gallery_page.html")

# Projects Page
def projects_page(request:HttpRequest):
    return render(request,"know_me/projects_page.html")

# Courses Page
def courses_page(request:HttpRequest):
    courses = Course.objects.all()
    return render(request,"know_me/courses_page.html",{"courses":courses})


# Add Course Page
def add_course_page(request:HttpRequest):

    if request.method == "POST":
        
        if "image" in request.FILES:
            new_course = Course(title=request.POST["title"], about_course=request.POST["about_course"], image=request.FILES["image"],start_from=request.POST["start_from"],end_at=request.POST["end_at"],course_hours=request.POST["course_hours"])
        else:
            new_course = Course(title=request.POST["title"], about_course=request.POST["about_course"],start_from=request.POST["start_from"],end_at=request.POST["end_at"],course_hours=request.POST["course_hours"])
        new_course.save()
        return redirect("know_me:courses_page")
    
    return render(request,"know_me/add_course_page.html")

# Detail Courses Page
def detail_course_page(request:HttpRequest,course_id):
   
    course = Course.objects.get(id = course_id)
    
    return render(request,"know_me/detail_course_page.html",{"course":course})

# Delete Courses
def delete_course(request:HttpRequest,course_id):

    course = Course.objects.get(id = course_id)
    course.delete()

    return redirect("know_me:courses_page")

# Update Course Page
def update_course_page(request:HttpRequest, course_id):

    course = Course.objects.get( id = course_id )
    iso_start_date = course.start_from.isoformat()
    iso_end_date = course.end_at.isoformat()

    if request.method == "POST":
        course.title = request.POST["title"]
        course.about_course = request.POST["about_course"]
        course.course_hours = request.POST["course_hours"]
        course.start_from = request.POST["start_from"]
        course.end_at = request.POST["end_at"]
        if "image" in request.FILES:
            course.image = request.FILES["image"]
        course.save()
        return redirect("know_me:detail_course_page", course_id = course.id)

    return render(request, 'know_me/update_course_page.html', {"course" : course,"iso_start_date":iso_start_date,"iso_end_date":iso_end_date}) 
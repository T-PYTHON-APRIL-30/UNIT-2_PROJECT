from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Course , Project ,Image

# Create your views here.

# Home Page
def home_page(request:HttpRequest):
    return render(request,"know_me/home_page.html")

# Gallery Page
def gallery_page(request:HttpRequest):
    return render(request,"know_me/gallery_page.html")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#--------------------------------- Project ----------------------------------
#///////////////////////////////////////////////////////////////////////////

# Projects Page
def projects_page(request:HttpRequest):
    projects = Project.objects.all()
    return render(request,"know_me/projects_page.html",{"projects":projects})

# Add Project Page
def add_project_page(request:HttpRequest):
    
    if request.method == "POST":

        if "project_logo" in request.FILES:
            new_project = Project(title=request.POST["title"], platform=request.POST["platform"],about_project=request.POST["about_project"],project_source=request.POST["project_source"],project_logo=request.FILES["project_logo"])
        else:
            new_project = Project(title=request.POST["title"], platform=request.POST["platform"],about_project=request.POST["about_project"],project_source=request.POST["project_source"])
        new_project.save()
        return redirect("know_me:projects_page")

    return render(request,"know_me/add_project_page.html")

# Detail Project Page
def detail_project_page(request:HttpRequest,project_id):
    #project.image_set.all()
    try:
        project = Project.objects.get(id = project_id)
        project_images = Image.objects.filter(project=project)
    except:
        return render(request, 'know_me/not_found.html')
    return render(request,"know_me/detail_project_page.html",{"project":project,"project_images":project_images})

# Delete Project
def delete_project(request:HttpRequest,project_id):

    project = Project.objects.get(id = project_id)
    project.delete()

    return redirect("know_me:projects_page")

# Update Project Page
def update_project_page(request:HttpRequest, project_id):

    project = Project.objects.get( id = project_id )

    if request.method == "POST":
        project.title = request.POST["title"]
        project.about_project = request.POST["about_project"]
        project.platform = request.POST["platform"]
        project.project_source = request.POST["project_source"]
        if "project_logo" in request.FILES:
            project.project_logo = request.FILES["project_logo"]
        project.save()
        return redirect("know_me:detail_project_page", project_id = project.id)

    return render(request, 'know_me/update_project_page.html', {"project" : project})    


def edit_project_image(request:HttpRequest, project_id):
    # to add image
    if request.method == "POST":
        project_object = Project.objects.get(id = project_id)
        if "images" in request.FILES:
            new_image = Image(project = project_object,images = request.FILES["images"])
        else:
            new_image = Image(project = project_object)
        new_image.save()
        return redirect("know_me:detail_project_page", project_id=project_id)
    
    # to display images in same page
    try:
        project = Project.objects.get( id = project_id )
        delete_images = Image.objects.filter(project=project)
    except:
        return redirect(request, 'know_me/not_found.html')
    
    return render(request,"know_me/edit_project_image.html",{"delete_images":delete_images,"project":project})


# Delete Project's image
def delete_image(request:HttpRequest, project_id):

    project = Image.objects.get(id = project_id)
    project.delete()
    return redirect("know_me:detail_project_page",{"project":project})

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#------------------------------- Course -------------------------------
#/////////////////////////////////////////////////////////////////////

# Courses Page
def courses_page(request:HttpRequest):
    if "presented_by" in request.GET:
        courses = Course.objects.filter(presented_by=request.GET["presented_by"])
    else:
        courses = Course.objects.all()
    return render(request,"know_me/courses_page.html",{"courses":courses})


# Add Course Page
def add_course_page(request:HttpRequest):
    if request.method == "POST":
        if "image" in request.FILES:
            new_course = Course(title=request.POST["title"], about_course=request.POST["about_course"], image=request.FILES["image"],start_from=request.POST["start_from"],end_at=request.POST["end_at"],course_hours=request.POST["course_hours"],presented_by = request.POST["presented_by"])
        else:
            new_course = Course(title=request.POST["title"], about_course=request.POST["about_course"],start_from=request.POST["start_from"],end_at=request.POST["end_at"],course_hours=request.POST["course_hours"],presented_by = request.POST["presented_by"])
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
        course.presented_by = request.POST["presented_by"]
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
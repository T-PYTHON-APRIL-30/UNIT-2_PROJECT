from django.urls import path
from . import views

app_name = "know_me"

urlpatterns = [ 
    path("", views.home_page, name="home_page"),
    path("gallery/", views.gallery_page, name="gallery_page"),
    path("projects/", views.projects_page, name="projects_page"),
    path("all/courses/", views.courses_page, name="courses_page"),
    path("add/courses/", views.add_course_page, name="add_course_page"),
    path("detail/courses/<course_id>/", views.detail_course_page, name="detail_course_page"),
    path("delete/courses/<course_id>/", views.delete_course, name="delete_course"),
]
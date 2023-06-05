from django.urls import path
from . import views

app_name = "know_me"

urlpatterns = [ 
    path("", views.home_page, name="home_page"),
    path("gallery/", views.gallery_page, name="gallery_page"),
# Projects
    path("projects/", views.projects_page, name="projects_page"),
    path("add/projects/", views.add_project_page, name="add_project_page"),
    path("detail/projects/<project_id>", views.detail_project_page, name="detail_project_page"),
    path("delete/projects/<project_id>/", views.delete_project, name="delete_project"),
    path("update/projects/<project_id>/", views.update_project_page, name="update_project_page"),
# Courses
    path("courses/", views.courses_page, name="courses_page"),
    path("add/courses/", views.add_course_page, name="add_course_page"),
    path("detail/courses/<course_id>/", views.detail_course_page, name="detail_course_page"),
    path("delete/courses/<course_id>/", views.delete_course, name="delete_course"),
    path("update/courses/<course_id>/", views.update_course_page, name="update_course_page"),

]
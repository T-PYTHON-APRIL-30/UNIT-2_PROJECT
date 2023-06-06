from django.urls import path
from . import views

app_name = "personal_app"

urlpatterns = [
    path('home/', views.home_page, name = "home_page"),
    path('gallery/', views.gallery_page, name = "gallery_page"),
    path('add/', views.add_contact, name = "add_contact"),
    path('read/', views.read_contact, name = "read_contact"),
    path('add/project/', views.add_project, name = "add_project"),
    path('project/details/<project_id>/', views.project_details, name ="project_details"),
    path("delete/<project_id>",views.delete_project,name="delete_project"),
]
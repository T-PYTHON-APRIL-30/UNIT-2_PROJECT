from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.home, name = "home"),
    path("resume", views.resume, name = "resume"),
    path("contact", views.add_contact, name = "contact"),
    path("projects", views.projects, name = "projects"),
]

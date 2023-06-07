from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.home, name = "home"),
    path("resume", views.resume, name = "resume"),
    path("contact", views.add_contact, name = "contact"),
    path("add/review", views.add_review, name = "review"),
    path("show/review", views.add_review, name = "showReviews"),
    path("projects", views.projects, name = "projects"),
]

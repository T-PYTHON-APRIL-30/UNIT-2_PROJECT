from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("career", views.career, name="career"),
    path("interests", views.interests, name="interests"),
    path("contact_me", views.contact_me, name="contact_me"),
]

from django.urls import path
from . import views

app_name = "profile_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("about", views.about_page, name="about_page"),
    path("skills", views.skill_page, name="skills_page"),
    path("contacts", views.contact_page, name="contacts_page"),
    path("projects", views.project_page, name="projects_page"),
    path("message", views.message_cards, name="message_cards")




]

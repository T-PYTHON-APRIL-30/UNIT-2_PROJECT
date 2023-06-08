from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
path("", views.index_page, name="index_page"),
path("myjourney/football/", views.football_page, name="football_page"),
path("myjourney/writing/", views.writing_page, name="writing_page"),
path("myjourney/software/", views.software_page, name="software_page"),
path("myjourney/contact/", views.contact, name="contact"),
path("myjourney/contact/success/", views.Submission, name="Submission"),
path("myjourney/not_ready/", views.not_ready, name="not_ready"),
path("myjourney/damn/", views.damn, name="404"),
path("myjourney/project/", views.project_view, name="project"),
path("myjourney/<novel_id>/details", views.book, name="details"),


]
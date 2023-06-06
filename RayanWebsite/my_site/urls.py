from django.urls import path
from . import views


app_name = "my_site"

urlpatterns = [ 
    path("", views.home_page, name="home_page"),
    path("about/",views.about, name="about_page" ),
    path("interests/", views.interests, name="interests_page"),
    path("skills/", views.skills, name="skills_page"),
    path("contact/", views.contact, name="contact_page"),
    path("feedback/", views.feedback, name="feedback_page"),
    path("delete/<comment_id>/", views.delete, name="delete_page"),

]
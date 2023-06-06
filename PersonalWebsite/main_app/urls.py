from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("page/blog", views.blog_page, name="blog_page"),
    path("page/testing", views.testing_page, name="testing_page"),
    path("page/add/", views.add_post, name="add_post"),
    path("page/details/<post_id>/", views.detail_page, name="detail_page"),
    path("page/contact", views.contact_page, name="contact_page"),
    path("page/about", views.about_page, name="about_page"),
    path("page/projects", views.projects_page, name="projects_page"),





]
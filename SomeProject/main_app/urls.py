from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contect/", views.contact_me, name="contect_me"),
    path("blog/", views.blog_page, name="blog_page"),
    path("blog/2", views.blog_page2,name="blog2_page")
]
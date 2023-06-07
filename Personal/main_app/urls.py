from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("test/", views.test_page, name="test_page"),
    path("", views.home_page, name="home_page"),
    path("contact/me/", views.contact_me, name="contact_me"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/read/", views.read_blogs, name="read_blogs"),
]
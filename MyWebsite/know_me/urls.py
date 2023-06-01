from django.urls import path
from . import views

app_name = "know_me"

urlpatterns = [ 
    path("", views.home_page, name="home_page"),
]
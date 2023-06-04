from django.urls import path, include
from . import views

app_name = "personal_app"

urlpatterns = [
    path('home/', views.home_page, name = "home_page"),
    path('gallery/', views.gallery_page, name = "gallery_page"),
]
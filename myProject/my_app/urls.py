from django.urls import path
from . import views

app_name="my_app"

urlpatterns = [
    path("",views.about_page,name="about_page"),
    path('myproject/',views.myproject_page,name="myproject_page"),
    path("skills/",views.skill_page,name="skill_page")
]

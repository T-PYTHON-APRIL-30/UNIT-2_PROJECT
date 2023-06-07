from django.urls import path
from . import views

app_name= "main_app"

urlpatterns=[
    path('',views.home_page ,name="home_page"),
    path('add/project/',views.add_project,name="add_project"),
    path("delete/<project_id>",views.delete_project,name="delete_project"),
    path('project/<project_id>/detail/',views.project_detail ,name="project_detail"),
    path('read/message/',views.read_message,name="read_message"),
    path('add/message/',views.add_message,name="add_message"),
    path('callOfduty/game/',views.game_one,name="game_one"),
    path('overwatch/game/',views.game_two,name="game_two"),
    path('rocket/game/',views.game_three,name="game_three"),
    path('aboutMe/',views.about_me,name="about_me")

]
from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("blogs/add/", views.add_blog, name="add_blog"),
    path("", views.index_page, name="index_page"),
    path("blogs/details/<blog_id>/", views.blog_detail, name="blog_detail"),
    path("blogs/update/<blog_id>/", views.update_blog, name="update_blog"),
    path("blogs/delete/<blog_id>/", views.delete_game, name="delete_game"),
    path("blogs/<blog_id>/review/add/", views.add_review, name="add_review"),
    path("perosnal/", views.perosnal_page, name="perosnal_page"),
    path("contect/", views.contact_me, name="contect_me"),
    path("about/", views.about_me, name="about_me"),
]
from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.index_page, name="index_page"),
    path("about/me", views.about_me, name="about_me"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact/with/me", views.contact, name="contact"),
    path("submit/done", views.submit_done, name="submit_done"),

]

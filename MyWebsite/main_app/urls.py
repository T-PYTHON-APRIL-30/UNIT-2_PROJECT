from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('add', views.add_page, name = 'add_page'),
    path('', views.home_page, name = 'home_page'),
    path('about/', views.about_page, name = 'about_page'),
    path('projects/', views.projects_page, name = 'projects_page'),
    path('projects/<project_id>', views.projects_detial_page, name = 'projects_detial_page'),
    path('projects/<project_id>/update', views.update_page, name = 'update_page'),
    path('contact/', views.contact_page, name = 'contact_page')
]

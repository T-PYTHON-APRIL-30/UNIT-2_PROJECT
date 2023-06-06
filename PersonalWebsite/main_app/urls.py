from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('contactor/<contactor_id>/', views.contactor, name='contactor')
]
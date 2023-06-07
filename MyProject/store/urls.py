from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    
    ]
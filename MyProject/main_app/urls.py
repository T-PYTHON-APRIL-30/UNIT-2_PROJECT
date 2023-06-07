from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('Subjects/new_subject/', views.newSubPage, name='newSubPage') ,
    path('subjects/details/<sub_id>/',views.detailsPage,name='detailsPage'),
    path("posts/delete/<sub_id>/", views.deleteSub, name="deleteSub"),
    path('search/',views.searchPage,name='searchPage'),

]
from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about', views.about_page, name='about_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('soon_page', views.soon_page, name='soon_page'),
    path('add_painting', views.add_painting, name='add_painting'),
    path('manual', views.manual, name='manual'),
    path('digital', views.digital, name='digital'),
    #path('animal', views.animal, name='animal'),
    path('web_design', views.web_design, name='web_design'),
    path('comments/<post_id>', views.comments, name='comments'),
    path("delete/<post_id>/", views.delete_post, name="delete_post"),
    path('update_post/<post_id>', views.update_post, name='update_post'),
    path("comments/<post_id>/review/", views.add_review, name="add_review"),

]
from django.contrib import admin
from .models import CvFile, Project


# Register your models here.
admin.site.register(CvFile)
admin.site.register(Project)
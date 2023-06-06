from django.contrib import admin
from .models import CvFile, Project, Education, Experience, Skills, Courses


# Register your models here.
admin.site.register(CvFile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Courses)
from django.contrib import admin
from .models import Project, contact
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','date',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','send_at')

admin.site.register(Project,ProjectAdmin)
admin.site.register(contact,ContactAdmin)

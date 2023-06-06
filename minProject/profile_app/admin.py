from django.contrib import admin
from .models import Contact
# Register your models here.


class Msg_Info(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'message')


admin.site.register(Contact, Msg_Info)

from django.contrib import admin

# Register your models here.
from .models import novel,comment,inquiry


class TitleAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)

class NameAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'Novel')

class FullnameAdmin(admin.ModelAdmin):
    list_filter = ('fullname',)    
    list_display = ('fullname',)


admin.site.register(novel, TitleAdmin)
admin.site.register(comment, NameAdmin)
admin.site.register(inquiry, FullnameAdmin)




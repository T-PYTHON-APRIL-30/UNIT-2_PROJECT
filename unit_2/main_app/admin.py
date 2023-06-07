from django.contrib import admin
from .models import Movies_TV, Career

# Register your models here.


class Movies_TV_Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "imdb_rating",
        "type",
        "image",
        "release_date",
    )


class Career_Admin(admin.ModelAdmin):
    list_display = ("company", "position", "tasks", "logo")


admin.site.register(Career, Career_Admin)
admin.site.register(Movies_TV, Movies_TV_Admin)

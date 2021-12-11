from django.contrib import admin
from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date', 'slides_url',)
    search_fields = ('title', )


admin.site.register(Lecture, LectureAdmin)

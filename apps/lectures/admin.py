from django.contrib import admin

from .models import Lecture



class LectureAdmin(admin.ModelAdmin):
    list_display = ('title','lecturer_name','date')
    search_fields=('title','date')
    filter_field = ('lecturer_name')
 

admin.site.register(Lecture, LectureAdmin)
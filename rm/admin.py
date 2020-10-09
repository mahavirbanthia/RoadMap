from django.contrib import admin

# Register your models here.
from .models import Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)

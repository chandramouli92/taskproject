from django.contrib import admin

# Register your models here.
from .models import CourseForm
class AdminCourseForm(admin.ModelAdmin):
    list_display=['course_name','course_provider_name','image_representing_course','iconimage_course_provider','category','start_date','end_date']

admin.site.register(CourseForm,AdminCourseForm)
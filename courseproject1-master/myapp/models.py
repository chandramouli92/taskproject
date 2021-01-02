from django.db import models

# Create your models here.
class CourseForm(models.Model):
    course_name=models.CharField(max_length=120)
    course_provider_name=models.CharField(max_length=120)
    image_representing_course=models.ImageField(null=True,blank=True,upload_to='images')
    iconimage_course_provider=models.ImageField(null=True,blank=True,upload_to='images')
    category=models.CharField(max_length=120)
    start_date=models.DateField()
    end_date=models.DateField()


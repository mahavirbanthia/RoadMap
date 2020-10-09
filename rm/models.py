from django.db import models

# Create your models here.
class Course(models.Model):
    category = models.CharField(max_length = 300, default="individual")
    course_id = models.AutoField
    course_name = models.CharField(max_length=30)
   
    short_desc = models.CharField(max_length=5000,default="")
    brief_desc = models.TextField()
   
    img = models.ImageField(upload_to = "rm/images",default= "")
    display_img = models.ImageField(upload_to = "rm/images",default= "")
    status = models.BooleanField(default=False)
      


    def __str__(self):
        return self.course_name
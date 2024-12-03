from django.db import models

# Create your models here.
class dest_input(models.Model):
    dest_category=models.CharField(max_length=30)
    dest_title=models.CharField(max_length=50,default="TITLE")
    dest_image=models.ImageField(upload_to="static")
    dest_desc=models.TextField()
    dest_tips=models.TextField(default="un")
    dest_tip1=models.TextField()
    dest_tip2=models.TextField()
    dest_tip3=models.TextField()
    dest_tip4=models.TextField(default="BEST OF LUCK")
    dest_tip5=models.TextField(default="HAVE A GREAT TRIP")
  

   

from django.db import models



# Create your models here.
class Student(models.Model):
   name=models.CharField(max_length=30) 
   email=models.EmailField()
   subject=models.CharField(max_length=100)
   level=models.CharField(max_length=15)
   message=models.TextField()

category_field=(
    ("Course","Collegelist")
       
)

class Course(models.Model):
    faculty=models.CharField(max_length=150)
    amount=models.IntegerField(null=True)
    Image=models.ImageField() 
    level=models.CharField(max_length=150)

class Collegelist(models.Model):
    collegename=models.CharField(max_length=150)
    amount=models.IntegerField(null=True)
    enrollmentdate=models.DateField()
    level=models.CharField(max_length=150)
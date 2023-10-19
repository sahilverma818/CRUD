from django.db import models

# Create your models here.

class Student(models.Model):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    roll = models.IntegerField(primary_key=True)

    


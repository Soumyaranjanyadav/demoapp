from django.db import models

class studentsdata(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    assignment1=models.IntegerField()
    assignment2=models.IntegerField()
    assignment3=models.IntegerField()
    assignment4=models.IntegerField()
    Total=models.IntegerField(null=True)
    Avg=models.IntegerField(null=True)


# Create your models here.

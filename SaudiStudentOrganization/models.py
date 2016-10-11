from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    Frist_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=200)

class Responds(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Response_Date_Time = models.DateTimeField('date responded')

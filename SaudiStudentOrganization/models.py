from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    Frist_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=200)

class Post(models.Model):
    Post_ID = models.CharField(max_length=10)
    Post_Date_Time = models.DateTimeField('date post')

class Responds(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Response_Date_Time = models.DateTimeField('date responded')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Products(models.Model):
    Product_ID = models.CharField(max_length=10)
    Prodcut_Name = models.CharField(max_length=200)
    Prodcut_Type = models.CharField(max_length=20)
    Price = models.DecimalField(max_digits=8, decimal_places=2)

class Product_Type(models.Model):
    Product_Type_ID = models.CharField(max_length=10)
    Prodcut_Type_Name = models.CharField(max_length=200)

class Tours(models.Model):
    Tour_ID = models.CharField(max_length=10)
    Tour_Date_Time = models.DateTimeField('date tour')

class Student_Tour(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)


class Destination(models.Model):
    Dest_ID = models.CharField(max_length=10)
    Destination_Name = models.CharField(max_length=200)


class Tour_Destinations(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)


class Saudi_Group_Admins(models.Model):
    Admin_ID = models.CharField(max_length=10)
    Frist_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=200)

class Arrival(models.Model):
    Arrival_ID = models.CharField(max_length=10)
    Arrival_Date_Time = models.DateTimeField('date arrival')
    Flight_Feedback = models.CharField(max_length=200)


class Student_Arrival(models.Model):
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class WhatWeOffer(models.Model):
    overview = models.TextField(max_length=50)
    title = models.CharField(max_length=50)
    brief_overview = models.TextField(max_length=50)

    def __str__(self):
        return self.title

class University(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()

    def __str__(self):
        return self.name


class CourseAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Courses(models.Model):
    course_image = models.ImageField(blank = True, null = True)
    course_name = models.CharField(max_length=100)
    course_detail = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    available_seat = models.IntegerField()
    author = models.ForeignKey(CourseAuthor, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    teacher_image = models.ImageField(upload_to="teacher_pics")
    # teacher = models.ForeignKey(CourseAuthor,on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    description = models.TextField()

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name
    
    

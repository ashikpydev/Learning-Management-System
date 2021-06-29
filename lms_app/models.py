from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
import random

# Create your models here.

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
    course_detail = models.TextField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    available_seat = models.IntegerField()
    author = models.ForeignKey(CourseAuthor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
    


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    teacher_image = models.ImageField(upload_to="teacher_pics")
    # teacher = models.ForeignKey(CourseAuthor,on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Signup(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name
    
    
class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to='blog_pics')
    blog_content = models.TextField()
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    slug = models.SlugField(max_length= 250)
    publish_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(blank=True, null = True)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment



                                #online Quiz System



DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
        

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        verbose_name_plural = 'Results'

    def __str__(self):
        return str(self.pk)
    

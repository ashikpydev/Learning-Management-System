from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(WhatWeOffer)
admin.site.register(University)
admin.site.register(CourseAuthor)
admin.site.register(Courses)
admin.site.register(Teacher)
admin.site.register(Signup)
admin.site.register(Blog)
admin.site.register(Comment)



admin.site.register(Quiz)

class AnswerTabularInline(admin.TabularInline):
    model = Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','text', 'correct')
    list_filter = ['correct']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerTabularInline]
    list_display = ('text','quiz')
    list_filter = ['quiz']
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result)
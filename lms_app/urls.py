from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('courses', courses, name='courses'),
    path('teacher', teacher, name='teacher'),
    path('blog-sigle', blog_single, name='blog-single'),
    path('signup', sign_up, name = 'sign_up'),
    path('login', user_login, name='user_login'),
    path('logout',user_logout, name = 'logout'),

    
]

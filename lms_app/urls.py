from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('courses', courses, name='courses'),
    path('teacher', teacher, name='teacher'),
    path('signup', sign_up, name = 'sign_up'),
    path('login', user_login, name='user_login'),
    path('logout',user_logout, name = 'logout'),
    path('create-blog',CreateBlog.as_view(), name= 'create-blog'),
    
    path('blog',Bloglist.as_view(), name='blog'),
    path('blog-detail/<slug:slug>', blog_details, name='blog-detail'),

    path('quiz-list/', QuizListView.as_view(), name='quiz-list'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),


    
]

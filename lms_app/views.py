from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import *
# Create your views here.

def index(request):
    what_we_offer = WhatWeOffer.objects.all()
    university = University.objects.all()
    context ={'what_we_offer':what_we_offer, 'university':university}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def courses(request):
    all_courses=Courses.objects.all()
    context={'all_courses':all_courses}
    return render(request, 'courses.html', context)

def teacher(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'teacher.html', context)

def blog_single(request):
    return render(request, 'blog-single.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        address = request.POST['address']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        if password == retype_password:
            user = User.objects.create_user(username = username, password = password)
            new_user = Signup.objects.create(user = user, first_name = first_name, last_name= last_name, email= email, address = address, mobile_no = mobile_no)


    return render(request, 'signup.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            login_user = username
            d_user = Signup.objects.get(user__username = login_user)
            context = {'d_user':d_user, 'user':user}
        return render(request, 'index.html', context)

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')



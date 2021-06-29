from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView, View, TemplateView, DeleteView
import uuid
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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


def courses(request):
    all_courses=Courses.objects.all()
    context={'all_courses':all_courses}
    return render(request, 'courses.html', context)

def teacher(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'teacher.html', context)


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


class CreateBlog(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'login'
    template_name = 'create_blog.html'
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return redirect('/blog')

class Bloglist(ListView):
    context_object_name = 'blog'
    model = Blog
    template_name = 'blog.html'


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment =comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog-detail', kwargs = {'slug':slug}))
    return render(request, 'blog_details.html', context={'blog':blog, 'comment_form':comment_form})




                            #online test System start


class QuizListView(ListView):
    model = Quiz 
    template_name = 'take-test.html'

@login_required(login_url='/login')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz.html', {'obj': quiz})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
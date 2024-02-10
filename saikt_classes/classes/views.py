from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .models import *
from .forms import LoginForm

# Create your views here.

@login_required(login_url="login")
def index(request):
    try:
        if request.user.is_staff:
            groups = Group.objects.all()
        else:
            student = Student.objects.get(user = request.user)
            groups = Group.objects.filter(pk = student.course_id.pk)
        students_count = []
    

        for group in groups:
            students = Student.objects.filter(course_id = group.pk)
            students_count.append(len(students))


        context = {
            "title": "Группы",
            "groups": groups,
            "students_count": students_count
        }

        return render(request, 'classes/index.html', context)
    except:
        return render(request, 'classes/index.html')

@login_required(login_url="login")
def group(request, course_id):
    try:
        sender = Student.objects.get(user = request.user)
        if sender.course_id.pk != course_id and not request.user.is_staff:
            return redirect('index')

        course = Group.objects.get(pk = course_id)

        wd = course.weekdays.all()
        wd_output = ""
        for i in wd:
            wd_output += str(i) + ", "
        wd_output = wd_output[:-2]

        students = Student.objects.filter(course_id = course_id)

        if request.method == "POST":

            for student in students:
                xp_value = request.POST.get(str(student.pk))
                student.xp_score = student.xp_score + int(xp_value)
                student.save()
                
                #Логи
                now = datetime.now()
                datetime = now.strftime("%d/%m/%Y %H:%M:%S")


        context = {
            "title": f"{course.course} {wd_output} {course.time.strftime('%H:%M')}",
            "students": students,
            "student": sender
        }
        return render(request, 'classes/group.html', context)
    except:
        return render(request, 'classes/group.html')


def student(request):
    try:
        context = {
            "title": "Профиль"
        }
        return render(request, 'classes/student.html', context)
    except:
        return render(request, 'classes/student.html')

def login(request):
    try:
        if request.method == "GET":
            form = LoginForm()

            context = {
                "title": "Авторизация",
                "form": form
            }
            return render(request, 'classes/registration/login.html', context)
        
        else:
            form = LoginForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    auth_login(request, user)
                    return redirect('index')
            
            context = {
                "title": "Авторизация",
                "form": form
            }
            return render(request, 'classes/registration/login.html', context)
    except:
        return render(request, 'classes/registration/login.html')

    

def logout(request):
    return redirect("index")
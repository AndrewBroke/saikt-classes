from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

from datetime import datetime
from .models import *
from .forms import LoginForm

# Create your views here.

def main_page_view(request):
    return redirect('index')

@login_required(login_url="login")
def index(request):
    try:
        if request.user.is_staff:
            admin_course = Course.objects.get(name="Admin")
            groups = Group.objects.all().exclude(course=admin_course)
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
        try:
            sender = Student.objects.get(user = request.user)
            if sender.course_id.pk != course_id and not request.user.is_staff:
                return redirect('index')
        except:
            sender = Student.objects.get(name = "admin")

        course = Group.objects.get(pk = course_id)

        wd = course.weekdays.all()
        wd_output = ""
        for i in wd:
            wd_output += str(i) + ", "
        wd_output = wd_output[:-2]

        students = Student.objects.filter(course_id = course_id).order_by('-xp_score', 'surname')

        column_len = len(students) // 2
        if len(students) % 2 == 1:
            column_len += 1

        students1 = students[0:column_len]
        students2 = students[column_len: len(students)]


        if request.method == "POST":
            if validate_xp(request.POST, students):
                now = datetime.now()

                change_type = request.POST.get("type")

                description = f"Change xp values type: {change_type}"

                changes = {}
                for student in students:
                    xp_value = request.POST.get(str(student.pk))
                    student.xp_score = student.xp_score + int(xp_value)
                    student.save()

                    changes[str(student.pk)] = int(xp_value)

                logevent = LogEvent(description=description, datetime=now, user=sender, changes=changes)

                logevent.save()
                check_role(students)


        context = {
            "title": f"{course.course} {wd_output} {course.time.strftime('%H:%M')}",
            "students": students,
            "students1": students1,
            "students2": students2,
            "student": sender
        }
        return render(request, 'classes/group.html', context)
    except Exception as e:
        print(e)
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

def logs(request):

    logs = LogEvent.objects.all()

    context = {
            "title": "Логи",
            "logs": logs
    }

    return render(request, 'classes/logs.html', context)


def validate_xp(data, students):
    for student in students:
        xp_value = data.get(str(student.pk))

        try: 
            int(xp_value) 
            print("True")
            return True
        except:
            print("False")
            return False

        # if not xp_value.isdigit():
        #     print("не цифра")
        #     return False
        # if int(xp_value) > 10 or int(xp_value) < -10:
        #     return False

 

def check_role(students):
    roles = Role.objects.all().order_by('target_xp')
    for student in students:
        if student.role:
            
            #ищем индекс нынешней роли (так как у QuerySet нет index() я просто написал свой *- * )
            current_role = Role.objects.get(pk = student.role.pk)
            for i in range(len(roles)):
                if roles[i] == current_role:
                    role_index = i
                    break
                else:
                    role_index = -1

            #трай нужен чтобы если у студента и так максимальная роль не вылезла ошибка а просто не изменялась роль
            try:
                #цикл я сделал чтобы если резко перейти с 1 роли на несколько вперёд ничего не поломалось
                while True:

                    #если баллов меньше чем нужно для нашей корректной роли
                    if student.xp_score < student.role.target_xp:
                        student.role = roles[role_index - 1]
                        role_index -= 1
                        student.save()
                        continue
                    #если больше
                    elif student.xp_score >= roles[role_index + 1].target_xp:
                        student.role = roles[role_index + 1]
                        role_index += 1
                        student.save()
                        continue
                    else:
                        break
            except Exception as e:
                print(e)
            return
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    groups = Group.objects.all()
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

def group(request, course_id):
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


    context = {
        "title": f"{course.course} {wd_output} {course.time.strftime('%H:%M')}",
        "students": students
    }
    return render(request, 'classes/group.html', context)


def student(request):
    context = {
        "title": "Профиль"
    }
    return render(request, 'classes/student.html', context)

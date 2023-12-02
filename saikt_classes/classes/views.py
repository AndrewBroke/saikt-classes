from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "title": "Классы"
    }
    return render(request, 'classes/index.html', context)

def group(request):
    context = {
        "title": "Группа"
    }
    return render(request, 'classes/group.html', context)


def student(request):
    context = {
        "title": "Профиль"
    }
    return render(request, 'classes/student.html', context)
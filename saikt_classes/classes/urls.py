from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/", views.group, name="group"),
    path("student/", views.student, name="student")
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:course_id>/", views.group, name="group"),
    path("student/", views.student, name="student"),
    # path("login/", views.login, name="login")
]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:course_id>/", views.group, name="group"),
    path("student/", views.student, name="student"),
    # path("login/", views.login, name="login")
    path("logout/", auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name="logout"),
    path("logs/", views.logs, name="logs"),
    path("achievments/", views.achievements, name="achievments")
]
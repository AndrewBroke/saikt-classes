from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

class Weekdays(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

class Group(models.Model):
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE
    )
    weekdays = models.ManyToManyField(Weekdays)
    time = models.DateTimeField()

class Role(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

class Achievement(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(blank=True, upload_to='images/')

class Student(models.Model):
    course_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    xp_score = models.IntegerField(null=False, default=0)
    age = models.IntegerField(null=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    surname = models.CharField(max_length=150, null=False, blank=False)
    achievement = models.ManyToManyField(Achievement)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, null=True)
    is_right_hand = models.BooleanField(default=False)

class LogEvent(models.Model):
    description = models.TextField(null=False, blank=True)
    datetime = models.DateTimeField()
    user = models.ManyToManyField(Student)
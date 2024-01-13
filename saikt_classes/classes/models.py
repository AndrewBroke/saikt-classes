from django.db import models
from django import forms

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(upload_to='courses/', blank=True)
    def __str__(self):
        return self.name

class Weekdays(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    shortname = models.CharField(max_length=150, null=True, blank=True, default="None")
    def __str__(self):
        return self.shortname

class Group(models.Model):
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE
    )
    weekdays = models.ManyToManyField(Weekdays)
    time = models.TimeField()

    def str(self):
        wd = self.weekdays.all()
        wd_output = ""
        for i in wd:
            wd_output += str(i) + ", "
        wd_output = wd_output[:-2]
        return str(self.course) + " | " + wd_output

class Role(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(blank=True, upload_to='achivments/')
    description = models.TextField(null=False, blank=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    course_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    xp_score = models.IntegerField(null=False, default=0)
    age = models.IntegerField(null=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    surname = models.CharField(max_length=150, null=False, blank=False)
    achievement = models.ManyToManyField(Achievement, null=True, blank=True)
    role = models.ForeignKey(
        'Role', 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )
    is_right_hand = models.BooleanField(default=False)
    def __str__(self):
        return self.name + " || " + str(self.course_id)

class LogEvent(models.Model):
    description = models.TextField(null=False, blank=True)
    datetime = models.DateTimeField()
    user = models.ManyToManyField(Student)
    def __str__(self):
        return self.datetime
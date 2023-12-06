from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Weekdays)
admin.site.register(Group)
admin.site.register(Role)
admin.site.register(Achievement)
admin.site.register(Student)
admin.site.register(LogEvent)
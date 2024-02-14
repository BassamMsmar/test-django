from django.contrib import admin
from simple_history import register
from django.contrib.auth.models import User


from .models import Student


# Register your models here.
admin.site.register(Student)
register(User)
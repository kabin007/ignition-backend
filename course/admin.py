from django.contrib import admin
from .models import Course,Faculty

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Course)
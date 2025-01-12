from django.contrib import admin
from .models import Student,StudyPreferences,EducationBackground

# Register your models here.
admin.site.register(Student)
admin.site.register(StudyPreferences)
admin.site.register(EducationBackground)
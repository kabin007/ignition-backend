from django.contrib import admin
from .models import Student,StudyPreferences,EducationBackground,Contact,Address,BasicInfo

# Register your models here.
admin.site.register(Student)
admin.site.register(StudyPreferences)
admin.site.register(EducationBackground)
admin.site.register(BasicInfo)
admin.site.register(Contact)
admin.site.register(Address)
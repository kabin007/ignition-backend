from rest_framework import serializers
from .models import Course,Faculty

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields="__all__"


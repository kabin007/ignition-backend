from rest_framework import serializers
from .models import Student, EducationBackground, StudyPreferences
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']  

        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print('User sent password',password)

        try:
            student = Student.objects.get(email=email)
            print('Found Student password',student.password)
            
            if not check_password(password, student.password):
                raise AuthenticationFailed("Invalid email or password")

            data['user'] = student
            return data
            
        except Student.DoesNotExist:
            raise AuthenticationFailed("Invalid email or password")
    
class EducationBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationBackground
        fields = '__all__'


class StudyPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPreferences
        fields = '__all__'

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from .models import Student, EducationBackground, StudyPreferences,Contact,BasicInfo,Address
import jwt
from datetime import datetime, timedelta, timezone 
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

#import serializers
from .serializers import (
    StudentSerializer,
    EducationBackgroundSerializer, StudyPreferencesSerializer,
    RegisterSerializer, LoginSerializer,AddressSerializer,ContactSerializer,BasicInfoSerializer
)


# Student ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=RegisterSerializer

    def perform_create(self, serializer):
        # Hash the password before saving
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class=RegisterSerializer
  
    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve the authenticated user
        user = serializer.validated_data['user']

        #check if its the user's first login
        is_first_login=user.is_first_login

        if is_first_login:
            #set the first login to false
            user.is_first_login=False
            user.save()


        # payload required for jwt generation
        payload = {
            'user_id': user.uuid,
            'email': user.contact.email,
            'exp': datetime.now(timezone.utc) + timedelta(seconds=settings.JWT_EXPIRATION_TIME),
            'iat': datetime.now(timezone.utc),
}
        
        #generate the token using payload,jwt secret key and hs256 algorithm
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')

        return Response({
            'token': token,
            'user': {
                'id': user.uuid,
                'full_name': user.basic_info.first_name,
                'email': user.contact.email,
                'isFirstLogin':user.is_first_login,
            }
        }, status=status.HTTP_200_OK)





# EducationBackground ViewSet
class EducationBackgroundViewSet(viewsets.ModelViewSet):
    queryset = EducationBackground.objects.all()
    serializer_class = EducationBackgroundSerializer


# StudyPreferences ViewSet
class StudyPreferencesViewSet(viewsets.ModelViewSet):
    queryset = StudyPreferences.objects.all()
    serializer_class = StudyPreferencesSerializer


class BasicInfoViewSet(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import FacultyViewSet,CourseViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'faculty',FacultyViewSet ,basename='faculty')
router.register(r'',CourseViewSet ,basename='course')

urlpatterns=[
    path('',include(router.urls))
]
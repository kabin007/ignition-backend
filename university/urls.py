from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UniversityViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'',UniversityViewSet ,basename='university')

urlpatterns=[
    path('',include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,LoginViewSet,RegisterViewSet,
    EducationBackgroundViewSet, StudyPreferencesViewSet
)

router = DefaultRouter()
router.register('student',StudentViewSet, basename='student')
router.register('login', LoginViewSet, basename='login')
router.register('register', RegisterViewSet, basename='register')
router.register('education', EducationBackgroundViewSet, basename='education')
router.register('preferences', StudyPreferencesViewSet, basename='preferences')

urlpatterns = [
    path('', include(router.urls)),
]

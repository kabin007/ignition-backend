from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import DocumentViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'',DocumentViewSet,basename='document')

urlpatterns=[
    path('',include(router.urls))
]
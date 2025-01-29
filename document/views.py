from django.shortcuts import render
from .models import Document
from .serializers import DocumentSerializer
from rest_framework import viewsets

# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    queryset=Document.objects.all()
    serializer_class=DocumentSerializer
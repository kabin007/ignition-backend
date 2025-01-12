
from rest_framework import viewsets
from .models import University
from .serializers import UniversitySerializer

#viewset to handle universites detail
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


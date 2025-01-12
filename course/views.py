from .serializers import FacultySerializer,CourseSerializer
from rest_framework import viewsets
from .models import Course,Faculty
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    @action(detail=False, methods=['post'], url_path='search')
    def search_courses(self, request):
        faculty_id = request.data.get('faculty')  # Get faculty ID from query params
        country_id = request.data.get('country')    # Get country name from query params

        #output the faculty_id and country_id for debug
        print(f'Received Data: faculty_id:{faculty_id},country_id:{country_id}')

        if not faculty_id or not country_id:
            return Response(
                {"error": "Both 'faculty' and 'country' parameters are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter courses based on faculty and country
        courses = Course.objects.filter(
            faculty__id=faculty_id,
            university__country__id=country_id  
        )
        print(courses)
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FacultyViewSet(viewsets.ModelViewSet):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer

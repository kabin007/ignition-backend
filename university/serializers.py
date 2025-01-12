from rest_framework import serializers
from .models import University


#serializer for university
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = [  'id',
                    'name',
                    'location', 
                    'established_year', 
                    'website', 
                    'admission_requirements',
                    'contact_email',
                    'contact_phone',
                    'accreditation',
                    'rank',
                ]

  

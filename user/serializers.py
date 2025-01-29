from rest_framework import serializers
from .models import Student, EducationBackground, StudyPreferences, BasicInfo, Contact, Address
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    basic_info = BasicInfoSerializer()
    contact = ContactSerializer()
    address = AddressSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'


    def update(self, instance, validated_data):
        # Extract the nested data for each serializer
        basic_info_data = validated_data.pop('basic_info', None)
        contact_data = validated_data.pop('contact', None)
        address_data = validated_data.pop('address', None)
        
        # Update the Student model instance with the top-level fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle the nested BasicInfo update
        if basic_info_data:
            for attr, value in basic_info_data.items():
                if attr != 'password':  # Do not update password
                    setattr(instance.basic_info, attr, value)
            instance.basic_info.save()

        # Handle the nested Contact update
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contact, attr, value)
            instance.contact.save()

        # Handle the nested Address update (if it exists)
        if address_data:
            if instance.address is None:  # If address does not exist, create one
                instance.address = Address.objects.create(**address_data)
            else:
                for attr, value in address_data.items():
                    setattr(instance.address, attr, value)
                instance.address.save()

        return instance


class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['full_name', 'email', 'phone', 'password']

    def create(self, validated_data):
        # Create BasicInfo instance
        basic_info = BasicInfo.objects.create(
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )

        # Create Contact instance
        contact = Contact.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone']
        )

        # Create Student instance
        student = Student.objects.create(
            basic_info=basic_info,
            contact=contact
        )

        return student

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print('User sent password', password)

        try:
            # Find student by email through Contact relation
            student = Student.objects.get(contact__email=email)
            print('Found Student password', student.basic_info.password)
            
            if not check_password(password, student.basic_info.password):
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
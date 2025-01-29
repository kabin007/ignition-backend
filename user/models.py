
from django.db import models
from course.models import Faculty
from country.models import Country
from document.models import Document



#stores student address
class Address(models.Model):
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=50)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.city},{self.city}'

#stores student contact
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email


#model to keep track of students education background
class EducationBackground(models.Model):
    highest_level_education = models.CharField(max_length=100)
    year_of_completion = models.CharField(max_length=4)
    country_of_education = models.CharField(max_length=100)
    obtained_marks = models.CharField(max_length=10)
    no_of_backlogs = models.CharField(max_length=10)
    education_gap = models.IntegerField()
    gap_reason = models.CharField(max_length=200)

    def __str__(self):
        return self.highest_level_education


class StudyPreferences(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    preferred_destination = models.ForeignKey(Country,on_delete=models.CASCADE)
    preferred_intake = models.CharField(max_length=50)

    def __str__(self):
        return f"Course Level: {self.faculty}, Destination: {self.preferred_destination}"

#stores student basic info
class BasicInfo(models.Model):
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=True,null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    marital_status=models.CharField(max_length=50)
    passport_no = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class Student(models.Model):
    uuid = models.AutoField(primary_key=True)
    basic_info=models.ForeignKey(BasicInfo,on_delete=models.SET_NULL, null=True, blank=True)
    contact=models.ForeignKey(Contact,on_delete=models.SET_NULL, null=True, blank=True)
    address=models.ForeignKey(Address,on_delete=models.SET_NULL, null=True, blank=True)
    educational_background=models.ForeignKey(EducationBackground,on_delete=models.SET_NULL, null=True, blank=True)
    study_preferences=models.ForeignKey(StudyPreferences,on_delete=models.SET_NULL, null=True, blank=True)
    documents=models.ForeignKey(Document,on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_first_login = models.BooleanField(default=True)  

    def __str__(self):
        return str(self.basic_info)

  

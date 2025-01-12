
from django.db import models
from course.models import Faculty
from country.models import Country

class Student(models.Model):
    uuid = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    passport_no = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


#model to keep track of students education background
class EducationBackground(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="education_backgrounds")
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
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="study_preferences")
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    preferred_destination = models.ForeignKey(Country,on_delete=models.CASCADE)
    preferred_intake = models.CharField(max_length=50)

    def __str__(self):
        return f"Course Level: {self.course_level}, Destination: {self.preferred_destination}"

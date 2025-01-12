from django.db import models
from university.models import University
    
#model to store the category of the courses
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#model to store the course detail
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50) 
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='faculty',default='')  
    university = models.ForeignKey(University, related_name='university', on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    prerequisites = models.TextField()
    credits = models.IntegerField()
    start_date = models.DateField()
    application_deadline = models.DateField()
    image = models.ImageField(upload_to='course_images/',default='')

    def __str__(self):
        return f"{self.name} ({self.university.name})"
    

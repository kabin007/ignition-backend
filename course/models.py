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
    COURSE_TYPES = [
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
    ]
    
    INTAKE_CHOICES = [
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
    ]

    name = models.CharField(max_length=255)
    course_type = models.CharField(max_length=50, choices=COURSE_TYPES,null=True)
    intakes = models.CharField(max_length=50, choices=INTAKE_CHOICES,null=True)
    url = models.URLField(max_length=500,null=True)
    description = models.TextField()
    duration = models.CharField(max_length=50) 
    faculty = models.ForeignKey(Faculty,on_delete=models.SET_NULL,related_name='faculty',null=True,default='')  
    university = models.ForeignKey(University, related_name='university', on_delete=models.SET_NULL,null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    prerequisites = models.TextField()
    credits = models.IntegerField()
    start_date = models.DateField()
    application_deadline = models.DateField()
    image = models.ImageField(upload_to='course_images/',default='')

    def __str__(self):
        return f"{self.name} ({self.university.name})"
    

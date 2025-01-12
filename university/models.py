from django.db import models
from country.models import Country

#model to store the university detail
class University(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rank = models.IntegerField(null=True, blank=True) 
    website = models.URLField()
    country=models.ForeignKey(Country,on_delete=models.CASCADE,default='')
    established_year = models.IntegerField()
    admission_requirements = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    accreditation = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return self.name

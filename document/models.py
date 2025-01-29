from django.db import models

# Create your models here.
class Document(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    document_file=models.FileField(upload_to='documents/')
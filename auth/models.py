from django.db import models
# Create your models here.
class Feature(models.Model):
    # id : int
    # name: str
    # details: str
    
    name = models.CharField(max_length=255)
    details= models.CharField(max_length=500)

from django.db import models

class Familiar(models.Model):
    name= models.CharField(max_length=100)
    years= models.IntegerField()
    married= models.BooleanField()
    

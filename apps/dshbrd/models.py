from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Destination(models.Model):
    destination = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    datefrom = models.DateField(auto_now_add=True)
    dateto = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User)    
    class Meta:
        db_table = 'destination'

class TravelPlan(models.Model):
    user_id = models.ManyToManyField(User)
    destination_id = models.ManyToManyField(Destination)
    class Meta:
        db_table = 'travelplan'
 
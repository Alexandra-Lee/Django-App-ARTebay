from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(unique=True, max_length=120)
    description = models.TextField(default='my description here')
    location = models.CharField(max_length=120, default='my location is ...') 
    occupation = models.CharField(max_length=120, null=True) 

    def __unicode__(self):
        return self.name +"      " + self.description + "  " + self.location

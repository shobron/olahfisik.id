from django.db import models
from olahfisik.choices import *

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=265, null=True)
    telephone = models.CharField(max_length=16, null=True)
    open = models.TimeField(null=True, blank=True)
    close = models.TimeField(null=True, blank=True)
    busy = models.TimeField(null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rating = models.CharField(max_length=16, null=True)
    type = models.CharField(choices = TYPE_CHOICES, max_length = 2)

    def __str__(self):
        return self.type
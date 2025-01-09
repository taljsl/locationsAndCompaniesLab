from django.db import models

# Create your models here.
class Place(models.Model):
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=2)
from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=32)
    industry = models.CharField(max_length=32)

    
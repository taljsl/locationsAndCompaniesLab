from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=32)
    industry = models.Charfield(max_length=32)

    
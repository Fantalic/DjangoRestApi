from django.db import models

# Create your models here.

class PvYield(models.Model):
    state = models.CharField(max_length=100)
    plz = models.CharField(max_length=10)
    yield_value = models.FloatField()
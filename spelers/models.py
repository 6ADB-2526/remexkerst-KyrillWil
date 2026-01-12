from django.db import models

# Create your models here.
class speler(models.Model):
    naam = models.CharField(max_length=25)
    voornaam = models.CharField(max_length=25)
    email = models.EmailField(max_length=125)

class match_punten(models.Model):
    nummerSpeler = models.IntegerField()
    punten = models.IntegerField(default=0)
    matchCode = models.IntegerField()

from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    address = models.CharField(max_length=50)

    class Meta:
        unique_together = (("city", "state", "address"),)


class Tournament(models.Model):
    name = models.CharField(max_length=25)
    location = models.ForeignKey('Location')
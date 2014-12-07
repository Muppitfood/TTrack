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
    location = models.ForeignKey('Location', null=True)


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Manager(models.Model):
    name = models.CharField(max_length=20)
    team = models.ForeignKey('Team')


class Player(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    bio = models.TextField()
    team = models.ForeignKey('Team')


class Sponsor(models.Model):
    name = models.CharField(max_length=25, unique=True)
    contract_end = models.DateField(db_index=True)
    contribution_size = models.DecimalField(max_digits=10, decimal_places=2)


class Match(models.Model):
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    round = models.IntegerField()
    team_one = models.ForeignKey('Team', related_name='team_one')
    team_two = models.ForeignKey('Team', related_name='team_two')
    tournament = models.ForeignKey('Tournament')

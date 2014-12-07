from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    address = models.CharField(max_length=50)

    class Meta:
        unique_together = (("city", "state", "address"),)

    def __str__(self):
        return '%s' % self.address


class Tournament(models.Model):
    name = models.CharField(max_length=25)
    location = models.ForeignKey('Location', null=True)

    def __str__(self):
        return '%s' % self.name


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)

    def __str__(self):
        return '%s' % self.name


class Manager(models.Model):
    name = models.CharField(max_length=20)
    team = models.ForeignKey('Team', null=True)

    def __str__(self):
        return '%s' % self.name


class Player(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=10)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    bio = models.TextField()
    team = models.ForeignKey('Team')

    def __str__(self):
        return '%s' % self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=25, unique=True)
    contract_end = models.DateField(db_index=True)
    contribution_size = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey('Team', null=True)

    def __str__(self):
        return '%s' % self.name


class Match(models.Model):
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    round = models.IntegerField()
    team_one = models.ForeignKey('Team', related_name='team_one')
    team_two = models.ForeignKey('Team', related_name='team_two')
    tournament = models.ForeignKey('Tournament')
    winner = models.ForeignKey('Team', related_name='Winner', null=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return '%s' % self.id

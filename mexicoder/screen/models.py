from django.db import models


class League(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    league = models.ForeignKey(League)
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    height = models.FloatField(default=1.75)
    position = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Coach(models.Model):
    team = models.ForeignKey(Team)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)

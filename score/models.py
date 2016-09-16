from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Player(models.Model):
    """ User model """
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    score = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

    
class Category(models.Model):
    """ Challenge's category """
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Challenge(models.Model):
    """ Challenge model """
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    description = models.TextField()
    data = models.ImageField(upload_to='data')
    score = models.IntegerField(default=0)
    flags = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Notice(models.Model):
    """ Notice model """
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now)
    def __unicode__(self):
        return self.title

class Solved(models.Model):
    """ Solved info model """
    player = models.ForeignKey(Player)
    challenge = models.ForeignKey(Challenge)
    score = models.IntegerField(default=0)
    time = models.DateTimeField(default=now)
    objects = models.Manager()

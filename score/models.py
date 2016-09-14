from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    """ User model """
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=32)
    mail = models.EmailField()
    score = models.IntegerField(default=0)
    def __unicode__(self):
        return self.display_name

    
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
    def __unicode__(self):
        return self.title

class Solved(models.Model):
    """ Solved info model """
    users = models.ForeignKey(Users)
    challenge = models.ForeignKey(Challenge)
    score = models.IntegerField(default=0)
    time = models.DateTimeField()
    def __unicode__(self):
        return self.users
    

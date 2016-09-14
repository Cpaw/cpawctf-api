from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    """ User model """
    display_name = models.CharField(max_length=32)
    mail = models.EmailField()
    score = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Challenge(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=50000)
    data = models.ImageField(upload_to='data')
    score = models.IntegerField(default=0)
    flags = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


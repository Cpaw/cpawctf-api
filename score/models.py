from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    """ User model """
    display_name = models.CharField(max_length=32)
    mail = models.EmailField()
    score = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=30)


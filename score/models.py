from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    display_name = models.CharField(max_length=32)
    mail = models.EmailField()
    score = models.IntegerField(default=0)


    

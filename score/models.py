from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class PlayerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not name:
            raise ValueError('Must have a name.')
        if not email:
            raise ValueError('Must have a email address.')
        
        email = PlayerManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password)
    
class Player(AbstractBaseUser):
    """ User model """
    name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    score = models.IntegerField(default=0)

    USERNAME_FIELD = 'name'
    
    objects = PlayerManager()

    class Meta:
        db_table = 'score'
        swappable = 'AUTH_USER_MODEL'
    
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
    def __unicode__(self):
        return self.title

class Solved(models.Model):
    """ Solved info model """
    users = models.ForeignKey(Users)
    challenge = models.ForeignKey(Challenge)
    score = models.IntegerField(default=0)
    time = models.DateTimeField()
    objects = models.Manager()

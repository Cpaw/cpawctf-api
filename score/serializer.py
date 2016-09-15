# coding: utf-8
from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('display_name', 'mail', 'score')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('category', 'name', 'description', 'data', 'score')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'description', 'priority')

class Solved(serializers.ModelSerializer):
    class Meta:
        model = Solved
        fields = ('users', 'challenge', 'score', 'time')



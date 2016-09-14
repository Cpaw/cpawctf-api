# coding: utf-8
from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user', 'display_name', 'mail', 'score')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields('name')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        fields('category', 'name', 'description', 'data', 'score')

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        fields('title', 'description', 'priority')

class Solved(serializers.ModelSerializer):
    class Meta:
        fields('users', 'challenge', 'score', 'time')



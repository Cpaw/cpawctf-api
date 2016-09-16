# coding: utf-8
from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'mail', 'password', 'score')
        write_only_fields = ('password')
        read_only_fields = ('name')

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
        fields = ('title', 'description', 'priority', 'created_at')

class Solved(serializers.ModelSerializer):
    class Meta:
        model = Solved
        fields = ('users', 'challenge', 'score', 'time')


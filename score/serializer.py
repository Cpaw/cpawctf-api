# coding: utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('username','email', 'password', 'score')
        read_only_fields = ('score',)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('username', 'score')
        
        
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


class SolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solved
        fields = ('users', 'challenge', 'score', 'time')


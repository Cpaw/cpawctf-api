# coding: utf-8
from rest_framework import serializers
from .models import *
from django.contrib.auth import hashers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user', 'display_name', 'mail', 'score')
        write_only_fields = ('user.password')
        read_only_fields = ('user.id')

        def create(self, validated_data):
            """ regist password """
            password = validated_data.get('password')
            validated_data['password'] = make_password(password)
            return Users.objects.create(**validated_data)

class AuthInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

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



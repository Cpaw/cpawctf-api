# coding: utf-8
import django_filters
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets, filters
from rest_framework_jwt.settings import api_settings
from .models import *
from .serializer import *
from .permissions import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class AuthView(generics.GenericAPIView):
    serializer_class = AuthInputSerializer
    def post(self, request):
        serializer = AuthInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)

        if not user:
            raise AuthenticationFailed()
        payload = jwt_payload_handler(user)
 
        return Response({
            'token': jwt_encode_handler(payload),
        })

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)    

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


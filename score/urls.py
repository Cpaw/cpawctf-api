# coding: utf-8
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UsersViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'challenge', ChallengeViewSet)
router.register(r'notice', NoticeViewSet)



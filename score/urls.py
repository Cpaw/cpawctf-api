# coding: utf-8
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users/(?P<user_id>.+)/$', PlayerViewSet)
router.register(r'ranking', ScorelistViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'challenge', ChallengeViewSet)
router.register(r'notice', NoticeViewSet)



from django.urls import path, include
from .views import RoomListCreateAPIView, RoomWithMessageAPIView, MessageCreateAPIView, \
    lobby, RoomViewSet, MessageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"rooms", RoomViewSet)
router.register(r"messages", MessageViewSet)


urlpatterns = [
    path("ws/", include(router.urls)),
]

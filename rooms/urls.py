from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, RoomPictureViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'room-pictures', RoomPictureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

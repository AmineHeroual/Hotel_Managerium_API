from rest_framework import viewsets
from .models import Room, RoomPicture
from .serializers import RoomSerializer, RoomPictureSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()# pylint: disable=no-member
    serializer_class = RoomSerializer

class RoomPictureViewSet(viewsets.ModelViewSet):
    queryset = RoomPicture.objects.all()# pylint: disable=no-member
    serializer_class = RoomPictureSerializer
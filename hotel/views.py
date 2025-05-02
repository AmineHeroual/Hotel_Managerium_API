from rest_framework import viewsets
from .models import Hotel, HotelPicture
from .serializers import HotelSerializer, HotelPictureSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()# pylint: disable=no-member
    serializer_class = HotelSerializer

class HotelPictureViewSet(viewsets.ModelViewSet):
    queryset = HotelPicture.objects.all()# pylint: disable=no-member
    serializer_class = HotelPictureSerializer

from rest_framework import serializers
from .models import Hotel, HotelPicture

class HotelPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPicture
        fields = ['id', 'image']

class HotelSerializer(serializers.ModelSerializer):
    pictures = HotelPictureSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'city', 'country', 'phone_number', 'email', 'pictures']

from rest_framework import serializers
from .models import Room, RoomPicture

class RoomPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPicture
        fields = ['id', 'image']
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

from rest_framework import serializers
from .models import Reservation
from users.models import User
from rooms.models import Room

class ReservationSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), required=False) # pylint: disable=no-member

    class Meta:
        model = Reservation
        fields = '__all__'

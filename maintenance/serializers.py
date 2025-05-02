from rest_framework import serializers
from .models import MaintenanceRequest
from rooms.models import Room
from users.models import User

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all()) # pylint: disable=no-member
    reported_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    technician = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

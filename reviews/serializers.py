from rest_framework import serializers
from .models import Review
from users.models import User
from rooms.models import Room

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), required=False) # pylint: disable=no-member

    class Meta:
        model = Review
        fields = '__all__'

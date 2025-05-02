from django.db import models
from hotel.models import Hotel

class Room(models.Model):
    ROOM_TYPE = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    )

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=ROOM_TYPE)
    features = models.TextField()
    discount_used = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number} ({self.type})"

class RoomPicture(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='room_pictures/')
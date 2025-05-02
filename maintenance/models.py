from django.db import models
from users.models import User
from rooms.models import Room

class MaintenanceRequest(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, related_name='reported_issues', on_delete=models.CASCADE)
    technician = models.ForeignKey(User, related_name='assigned_issues', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maintenance - {self.room.room_number} ({self.status})"# pylint: disable=no-member

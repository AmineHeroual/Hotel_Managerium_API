from django.contrib import admin
from .models import Room, RoomPicture

class RoomPictureInline(admin.TabularInline):
    model = RoomPicture
    extra = 1  # Show one empty image field by default
    max_num = 5  # Optional: Limit number of pictures per room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'room_number', 'type', 'price', 'discount_used', 'created_at')
    search_fields = ('name', 'room_number', 'hotel__name')
    list_filter = ('type', 'hotel__city', 'hotel__name')
    inlines = [RoomPictureInline]

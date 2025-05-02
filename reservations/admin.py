from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'room', 'start_date', 'end_date', 'status')
    search_fields = ('client__username', 'room__name')
    list_filter = ('status', 'start_date', 'end_date')

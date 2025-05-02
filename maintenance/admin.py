from django.contrib import admin
from .models import MaintenanceRequest

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('room', 'description', 'created_at', 'status')
    search_fields = ('room__name', 'description')
    list_filter = ('status', 'created_at')

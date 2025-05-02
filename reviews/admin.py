from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'room', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'room__name')
    list_filter = ('rating', 'created_at')


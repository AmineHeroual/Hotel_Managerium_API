from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'status', 'created_at')
    search_fields = ('client__username',)
    list_filter = ('status', 'created_at')


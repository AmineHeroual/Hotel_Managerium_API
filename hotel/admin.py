from django.contrib import admin
from .models import Hotel, HotelPicture

class HotelPictureInline(admin.TabularInline):
    model = HotelPicture
    extra = 1  # Number of empty image slots shown by default
    max_num = 5  # Optional: Limit the number of pictures

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'phone_number', 'email')
    search_fields = ('name', 'city', 'country')
    list_filter = ('city', 'country')
    inlines = [HotelPictureInline]

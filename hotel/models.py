from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)

class HotelPicture(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='hotel_pictures/')
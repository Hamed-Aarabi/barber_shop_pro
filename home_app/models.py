from django.db import models


class HomeInfo(models.Model):
    barber_name = models.CharField(max_length=100)
    barber_slogan = models.TextField()
    barber_logo = models.ImageField(upload_to='logo/')
    barber_book_logo = models.ImageField(upload_to='booking_logo/')

    def __str__(self):
        return self.barber_name



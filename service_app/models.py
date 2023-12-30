from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class PriceList(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='price_list/', null=True)

    def __str__(self):
        return self.title



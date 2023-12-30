from .models import *


def get_about_us(request):
    about_us = AboutUs.objects.last()
    return {'about_us': about_us}


def get_barber(request):
    barbers = Barber.objects.all()
    return {'barbers': barbers}

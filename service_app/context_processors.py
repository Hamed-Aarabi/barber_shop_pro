from .models import *


def get_service(request):
    services = Service.objects.all()
    return {'services': services}


def get_price_list(request):
    price_list = PriceList.objects.last()
    return {'price_list': price_list}

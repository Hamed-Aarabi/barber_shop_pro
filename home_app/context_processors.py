from .models import HomeInfo


def get_home_info(request):
    infos = HomeInfo.objects.last()
    return {'home_infos': infos}

from .models import *


def get_contact_us(request):
    contacts = Contactus.objects.last()
    return {'contacts': contacts}


def get_contact_social_media(request):
    contact_socials = SocialMediaContact.objects.all()
    return {'contact_socials': contact_socials}


def get_work_hour(request):
    work_hours = WorkHour.objects.last()
    return {'work_hours': work_hours}


def get_our_branch(request):
    our_branches = OurBranch.objects.all()
    return {'our_branches': our_branches}

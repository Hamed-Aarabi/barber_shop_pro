from django.db import models


class Contactus(models.Model):
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.phone


class WorkHour(models.Model):
    title = models.CharField(max_length=100)
    open_at = models.CharField(max_length=10)
    close_at = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}-->{self.open_at}-{self.close_at}'


class SocialMediaContact(models.Model):
    SOCIAL_MEDIA_ICONS = (
        ('bi-facebook', 'Facebook'),
        ('bi-instagram', 'Instagram'),
        ('bi-whatsapp', 'Whatsapp'),
        ('bi-twitch', 'Twitch'),
        ('bi-twitter', 'Twitter'),
        ('bi-telegram', 'Telegram'),
    )

    link = models.URLField(blank=True)
    icon = models.CharField(max_length=100, choices=SOCIAL_MEDIA_ICONS)

    def __str__(self):
        return self.icon


class OurBranch(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

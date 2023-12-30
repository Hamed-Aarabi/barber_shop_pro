from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Barber(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='barbers/')

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    SOCIAL_MEDIA_ICONS = (
        ('bi-facebook', 'Facebook'),
        ('bi-instagram', 'Instagram'),
        ('bi-whatsapp', 'Whatsapp'),
        ('bi-twitch', 'Twitch'),
        ('bi-twitter', 'Twitter'),
        ('bi-telegram', 'Telegram'),
    )

    barber = models.ForeignKey(Barber, related_name='socials', on_delete=models.CASCADE)
    link = models.URLField(blank=True)
    icon = models.CharField(max_length=100, choices=SOCIAL_MEDIA_ICONS)

    def __str__(self):
        return self.barber.name

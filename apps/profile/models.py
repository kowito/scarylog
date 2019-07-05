from stdimage import StdImageField
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = StdImageField(null=True,
                            blank=True,
                            upload_to='profile',
                            variations={
                                'retina': (960, 960, True),
                                'normal': (240, 240, True),
                                'thumbnail': (160, 160, True)}
                            )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    def get_picture_thumbnail(self):
        default = f"{settings.STATIC_URL}avatar.jpg"
        return f"{settings.MEDIA_URL}{self.photo.thumbnail}" if self.photo else default


User.profile = property(
    lambda u: UserProfile.objects.get_or_create(user=u)[0]
)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

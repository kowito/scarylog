from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import strip_tags

from django_extensions.db.fields import AutoSlugField
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField
import requests
from scarylog.settings import GOOGLE_API_KEY


class Story(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name=_("Story caption"))
    slug = AutoSlugField(populate_from='name', blank=True)
    __original_coordinate = None
    coordinate = PlainLocationField(based_fields=['name'], zoom=12, verbose_name=_("Location"))
    description = RichTextField(verbose_name=_("Story"))
    short_desc = RichTextField(null=True, blank=True)
    geocoding = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationship Fields
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="stories",
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name = _("story")
        verbose_name_plural = _("stories")

    def __init__(self, *args, **kwargs):
        super(Story, self).__init__(*args, **kwargs)
        self.__original_coordinate = self.coordinate

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        self.short_desc = strip_tags(self.description)[:1000]

        # Auto detect coordinate changed
        if self.coordinate and self.__original_coordinate != self.coordinate:
            endpoint = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={self.coordinate}&key={GOOGLE_API_KEY}'
            self.geocoding = requests.get(endpoint).json()

        super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('story_story_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('story_story_update', args=(self.slug,))

    def algolia_location(self):
        location = self.coordinate.split(",", 2)
        return float(location[0]), float(location[1])

    def google_place_id(self):
        if self.geocoding:
            results = self.geocoding.get('results')
            city = next(result for result in results if ('political' in result.get('types') and
                                                         (
                        'locality' in result.get('types') or
                        'administrative_area_level_1' in result.get('types')
                        )
            ))
            return city.get('place_id')

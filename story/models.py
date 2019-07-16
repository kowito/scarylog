from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import strip_tags
from django.utils.text import slugify


from django_extensions.db.fields import AutoSlugField
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField
import requests
from scarylog.settings import GOOGLE_API_KEY
from google.cloud import translate_v3beta1 as translate


def translation(project_id, text, from_lang, to_lang):
    client = translate.TranslationServiceClient()
    location = 'global'
    parent = client.location_path(project_id, location)
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type='text/plain',  # mime types: text/plain, text/html
        source_language_code=from_lang,
        target_language_code=to_lang)

    return response.translations[0].translated_text


class Story(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name=_("Story caption"))
    slug = models.CharField(max_length=300)
    coordinate = PlainLocationField(based_fields=['name'], zoom=12, verbose_name=_("Location"))

    description = RichTextField(verbose_name=_("Story"))
    short_desc = RichTextField(null=True, blank=True)
    geocoding = models.TextField(null=True, blank=True)
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

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        self.short_desc = strip_tags(self.description)[:1000]
        if not self.geocoding:
            endpoint = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={self.coordinate}&key={GOOGLE_API_KEY}'
            self.geocoding = requests.get(endpoint).json()
        self.slug = slugify(translation('scarylog-dceb3', self.name, 'th', 'en-US'))[:50]
        super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('story_story_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('story_story_update', args=(self.slug,))

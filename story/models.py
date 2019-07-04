from django.urls import reverse
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from django_extensions.db.fields import AutoSlugField
from location_field.models.plain import PlainLocationField
from ckeditor.fields import RichTextField


class Story(models.Model):

    # Fields
    name = models.CharField(max_length=255, verbose_name=_("Story caption"))
    slug = AutoSlugField(populate_from='name', blank=True)
    coordinate = PlainLocationField(based_fields=['name'], zoom=12, verbose_name=_("Location"))
    description = RichTextField(verbose_name=_("Story"))
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

    def get_absolute_url(self):
        return reverse('story_story_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('story_story_update', args=(self.slug,))

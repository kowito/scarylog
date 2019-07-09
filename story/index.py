from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Story


@register(Story)
class StoryIndex(AlgoliaIndex):
    fields = ('name', 'slug', 'coordinate', 'short_desc', 'geocoding', 'created_at', 'updated_at',)

    geo_field = 'coordinate'
    settings = {'searchableAttributes': ['name', 'short_desc']}
    index_name = 'story_index'

from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Story


@register(Story)
class StoryIndex(AlgoliaIndex):
    fields = ('name', 'slug', 'coordinate', 'google_place_id', 'description', 'created_at', 'updated_at',)
    geo_field = 'algolia_location'
    settings = {'searchableAttributes': ['name', 'description']}
    index_name = 'story_index'

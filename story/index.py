from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex
from .models import Story


@register(Story)
class StoryIndex(AlgoliaIndex):
    fields = ('name', 'slug', 'coordinate', 'description', 'created_at', 'updated_at',)
    geo_field = 'coordinate'
    settings = {'searchableAttributes': ['name', 'description']}
    index_name = 'story_index'

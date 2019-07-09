from django.apps import AppConfig
from django.conf import settings
import algoliasearch_django as algoliasearch


class StoryConfig(AppConfig):
    name = 'story'

    def ready(self):
        if not settings.DEBUG:
            Story = self.get_model('story')
            algoliasearch.register(Story, StoryIndex)

from modeltranslation.translator import translator, TranslationOptions
from apps.story.models import Story


class StoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )

translator.register(Story, StoryTranslationOptions)

from . import models
from . import serializers
from rest_framework import viewsets, permissions


class StoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Story class"""

    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer

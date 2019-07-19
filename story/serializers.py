from . import models

from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):
    storygallerys = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Story
        fields = (
            'pk',
            'name',
            'coordinate',
            'description',
            'created_at',
            'updated_at',
        )

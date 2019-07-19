from django.contrib import admin
from django import forms
from .models import Story


class StoryAdminForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = '__all__'


class StoryAdmin(admin.ModelAdmin):
    form = StoryAdminForm
    list_display = ['name', 'coordinate', 'created_at', 'updated_at']

admin.site.register(Story, StoryAdmin)

from django.contrib import admin
from apps.profile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone', 'city', 'country')
    search_fields = ['user__email']

admin.site.register(UserProfile, UserProfileAdmin)

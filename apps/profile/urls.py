from django.conf.urls import url

from apps.profile.views import *

urlpatterns = (
    url(r'^update/$', profile_update, name='profile_update_url'),
)

from django.conf.urls import url
from django.urls import include
from apps.profile.views import *

urlpatterns = (
    url(r'^update/$', profile_update, name='profile_update_url'),
    url(r'^picture/$', update_profile_picture_form, name='profile_picture_url'),
    url(r'^select2/', include('django_select2.urls')),
)

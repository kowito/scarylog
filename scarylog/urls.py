from django.contrib import admin
from django.urls import include, path
from story.views import StoryListView
from scarylog import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', StoryListView.as_view(), name='home'),
    path('story/', include('story.urls')),
    path('profile/', include('apps.profile.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

from django.urls import path
from rest_framework import routers
from django.conf.urls import url

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'story', api.StoryViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    # path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Story
    # path('', views.StoryListView.as_view(), name='home'),
    path('create/', views.StoryCreateView.as_view(), name='story_story_create'),
    path('detail/<str:name>/', views.StoryDetailView.as_view(), name='story_story_detail'),
    path('update/<int:pk>/', views.StoryUpdateView.as_view(), name='story_story_update'),
    path('map/', views.map_view, name="map_view"),
)

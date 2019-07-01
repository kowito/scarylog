from django.urls import path, include
from rest_framework import routers

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
    path('detail/<slug:slug>/', views.StoryDetailView.as_view(), name='story_story_detail'),
    path('update/<slug:slug>/', views.StoryUpdateView.as_view(), name='story_story_update'),
)

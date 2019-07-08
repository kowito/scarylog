from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.http import JsonResponse
from algoliasearch.search_client import SearchClient
from django.conf import settings

from .models import Story
from .forms import StoryForm

import os


class StoryListView(ListView):
    model = Story
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
        return context


class StoryCreateView(CreateView):
    model = Story
    form_class = StoryForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StoryCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect(obj.get_absolute_url())


class StoryDetailView(DetailView):
    model = Story


@method_decorator(login_required, name='dispatch')
class StoryUpdateView(UpdateView):
    model = Story
    form_class = StoryForm


def map_view(request):
    return render(request, 'map_view.html', {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
    })


def ajax_get_stories(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    radius = request.GET.get('radius', None)

    client = SearchClient.create(settings.ALGOLIA_APP_ID, settings.ALGOLIA_ADMIN_API_KEY)
    story_index = client.init_index('story_index')
    data = story_index.search('', {
        'aroundLatLng': f'{lat},{lng}',
        'aroundRadius': radius,
    })
    return JsonResponse(data)

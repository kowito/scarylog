from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from algoliasearch_django import raw_search

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

    def get_object(self):
        return Story.objects.get(name=self.kwargs["name"])


@method_decorator(login_required, name='dispatch')
class StoryUpdateView(UpdateView):
    model = Story
    form_class = StoryForm


def map_view(request):
    return render(request, 'map_view.html', {
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY'),
    })


def ajax_get_stories(request):
    lat1 = request.GET.get('lat1', None)
    lng1 = request.GET.get('lng1', None)
    lat2 = request.GET.get('lat2', None)
    lng2 = request.GET.get('lng2', None)
    query = request.GET.get('query', '')

    params = {'insideBoundingBox': f'{lat1},{lng1},{lat2},{lng2}'}
    response = raw_search(Story, query, params)

    return JsonResponse(response)

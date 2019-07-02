from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Story
from .forms import StoryForm

import os


class StoryListView(ListView):
    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
        return context


@method_decorator(login_required, name='dispatch')
class StoryCreateView(CreateView):
    model = Story
    form_class = StoryForm


@method_decorator(login_required, name='dispatch')
class StoryDetailView(DetailView):
    model = Story


@method_decorator(login_required, name='dispatch')
class StoryUpdateView(UpdateView):
    model = Story
    form_class = StoryForm

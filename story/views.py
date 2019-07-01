from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Story
from .forms import StoryForm


class StoryListView(ListView):
    model = Story


class StoryCreateView(CreateView):
    model = Story
    form_class = StoryForm


class StoryDetailView(DetailView):
    model = Story


class StoryUpdateView(UpdateView):
    model = Story
    form_class = StoryForm

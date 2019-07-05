from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

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

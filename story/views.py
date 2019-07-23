from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from .models import Story
from .forms import StoryForm

from scarylog.settings import GOOGLE_API_KEY

import os


class StoryListView(ListView):
    model = Story
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['GOOGLE_API_KEY'] = GOOGLE_API_KEY
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
    context = {
        'GOOGLE_API_KEY': GOOGLE_API_KEY,
    }
    if request.user_agent.is_mobile or request.user_agent.is_tablet:
        template = 'mobile_index.html'
        context['stories'] = Story.objects.all()
    else:
        template = 'map_view.html'
    return render(request, template, context)

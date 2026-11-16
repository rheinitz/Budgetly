from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from common.mixins import DeleteFormInstanceMixin
from tags.forms import TagDeleteForm, TagForm
from tags.models import Tag


class TagListView(ListView):
    model = Tag


class TagDetailView(DetailView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm


class TagDeleteView(DeleteFormInstanceMixin, DeleteView):
    model = Tag
    form_class = TagDeleteForm
    success_url = reverse_lazy("tags:list")

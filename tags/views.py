from typing import Any

from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from common.mixins import DeleteFormInstanceMixin
from tags.forms import TagDeleteForm, TagForm
from tags.models import Tag


class TagListView(ListView):
    model = Tag

    def get_queryset(self):
        return super().get_queryset().annotate(transaction_count=Count("transactions"))


class TagDetailView(DetailView):
    model = Tag

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        transactions = self.object.transactions.with_related()
        context["transactions"] = transactions
        context["totals"] = transactions.totals()
        return context


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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["transaction_count"] = self.object.transactions.count()
        return context

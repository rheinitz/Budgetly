from datetime import date
from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from categories.models import Subcategory
from common.mixins import DeleteFormInstanceMixin, MonthMixin
from entries.forms import EntryDeleteForm, EntryForm
from entries.mixins import EntryMonthRedirectMixin
from entries.models import Entry
from entries.querysets import EntryQuerySet


def current_month(request: HttpRequest) -> HttpResponseRedirect:
    today = date.today()
    return redirect("entries:month", year=today.year, month=today.month)


class MonthEntriesView(MonthMixin, ListView):
    model = Entry
    template_name = "entries/entry_month.html"
    context_object_name = "entries"

    def get_queryset(self) -> EntryQuerySet:
        return Entry.objects.for_month(
            self.month_start.year,
            self.month_start.month,
        ).with_related()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["totals"] = self.object_list.totals()
        return context


class EntryCreateView(EntryMonthRedirectMixin, CreateView):
    model = Entry
    form_class = EntryForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["has_subcategories"] = Subcategory.objects.exists()
        return context


class EntryUpdateView(EntryMonthRedirectMixin, UpdateView):
    model = Entry
    form_class = EntryForm


class EntryDetailView(DetailView):
    queryset = Entry.objects.with_related()


class EntryDeleteView(EntryMonthRedirectMixin, DeleteFormInstanceMixin, DeleteView):
    model = Entry
    form_class = EntryDeleteForm

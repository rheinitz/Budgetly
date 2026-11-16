from datetime import date
from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from categories.models import Subcategory
from common.mixins import DeleteFormInstanceMixin, MonthMixin
from entries.choices import EntryPageSize
from entries.forms import EntryDeleteForm, EntryFilterForm, EntryForm
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


class EntryListView(ListView):
    model = Entry
    paginate_by = 10
    context_object_name = "entries"

    def get_paginate_by(self, queryset: EntryQuerySet) -> int:
        per_page = self.filter_form.cleaned_data.get("per_page")
        if per_page in EntryPageSize.values:
            return per_page
        return EntryPageSize.TEN

    def get_queryset(self) -> EntryQuerySet:
        data = self.request.GET.copy()
        if not data.get("per_page"):
            data["per_page"] = str(EntryPageSize.TEN)
        self.filter_form = EntryFilterForm(data)
        queryset = Entry.objects.with_related()
        if not self.filter_form.is_valid():
            return queryset
        cleaned = self.filter_form.cleaned_data
        return (
            queryset.search(cleaned["q"])
            .in_category(cleaned["category"])
            .with_tag(cleaned["tag"])
            .between(cleaned["start"], cleaned["end"])
            .order_by(cleaned["sort"] or "-date", "-pk")
        )

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["filter_form"] = self.filter_form
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

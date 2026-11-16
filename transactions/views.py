from datetime import date
from typing import Any

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from categories.models import Type
from common.mixins import DeleteFormInstanceMixin, MonthMixin
from transactions.choices import TransactionPageSize
from transactions.forms import TransactionDeleteForm, TransactionFilterForm, TransactionForm
from transactions.mixins import TransactionMonthRedirectMixin
from transactions.models import Transaction
from transactions.querysets import TransactionQuerySet


def current_month(request: HttpRequest) -> HttpResponseRedirect:
    today = date.today()
    return redirect("transactions:month", year=today.year, month=today.month)


class MonthTransactionsView(MonthMixin, ListView):
    model = Transaction
    template_name = "transactions/transaction_month.html"
    context_object_name = "transactions"

    def get_queryset(self) -> TransactionQuerySet:
        return Transaction.objects.for_month(
            self.month_start.year,
            self.month_start.month,
        ).with_related()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["totals"] = self.object_list.totals()
        return context


class TransactionListView(ListView):
    model = Transaction
    paginate_by = 10
    context_object_name = "transactions"

    def get_paginate_by(self, queryset: TransactionQuerySet) -> int:
        per_page = self.filter_form.cleaned_data.get("per_page")
        if per_page in TransactionPageSize.values:
            return per_page
        return TransactionPageSize.TEN

    def get_queryset(self) -> TransactionQuerySet:
        data = self.request.GET.copy()
        if not data.get("per_page"):
            data["per_page"] = str(TransactionPageSize.TEN)
        self.filter_form = TransactionFilterForm(data)
        queryset = Transaction.objects.with_related()
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


class TransactionCreateView(TransactionMonthRedirectMixin, CreateView):
    model = Transaction
    form_class = TransactionForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["has_types"] = Type.objects.exists()
        return context


class TransactionUpdateView(TransactionMonthRedirectMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm


class TransactionDetailView(DetailView):
    queryset = Transaction.objects.with_related()


class TransactionDeleteView(TransactionMonthRedirectMixin, DeleteFormInstanceMixin, DeleteView):
    model = Transaction
    form_class = TransactionDeleteForm

from typing import Any

from django.db.models import Count, RestrictedError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from categories.choices import Category
from categories.forms import TypeDeleteForm, TypeForm
from categories.models import Type
from common.mixins import DeleteFormInstanceMixin


class TypeListView(ListView):
    model = Type

    def get_queryset(self):
        return super().get_queryset().annotate(transaction_count=Count("transactions"))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        grouped = {}
        for category in Category:
            grouped[category] = []

        for budget_type in self.object_list:
            grouped[budget_type.category_choice].append(budget_type)

        context["category_groups"] = grouped
        return context


class TypeDetailView(DetailView):
    model = Type

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        transactions = self.object.transactions.with_related()
        context["transactions"] = transactions
        context["total"] = transactions.total_amount()
        return context


class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        category = self.request.GET.get("category")
        if category in Category.values:
            initial["category"] = category
        return initial


class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm


class TypeDeleteView(DeleteFormInstanceMixin, DeleteView):
    model = Type
    form_class = TypeDeleteForm
    success_url = reverse_lazy("types:list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["has_transactions"] = self.object.transactions.exists()
        return context

    def form_valid(self, form: TypeDeleteForm) -> HttpResponse:
        try:
            return super().form_valid(form)
        except RestrictedError:
            context = self.get_context_data(
                form=form,
                delete_error="This type was not deleted because it has transactions.",
            )
            return self.render_to_response(context)

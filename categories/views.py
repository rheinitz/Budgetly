from typing import Any

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from categories.choices import Category
from categories.forms import SubcategoryDeleteForm, SubcategoryForm
from categories.models import Subcategory
from common.mixins import DeleteFormInstanceMixin


class SubcategoryListView(ListView):
    model = Subcategory

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        grouped = {}
        for category in Category:
            grouped[category] = []

        for subcategory in self.object_list:
            grouped[subcategory.category_choice].append(subcategory)

        context["category_groups"] = grouped
        return context


class SubcategoryDetailView(DetailView):
    model = Subcategory


class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        category = self.request.GET.get("category")
        if category in Category.values:
            initial["category"] = category
        return initial


class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm


class SubcategoryDeleteView(DeleteFormInstanceMixin, DeleteView):
    model = Subcategory
    form_class = SubcategoryDeleteForm
    success_url = reverse_lazy("categories:list")

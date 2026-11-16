from typing import Any

from django.http import HttpRequest, HttpResponseBase

from common.utils import get_month_start_or_404, shift_month


class DeleteFormInstanceMixin:
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


class MonthMixin:
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        self.month_start = get_month_start_or_404(kwargs["year"], kwargs["month"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["month_start"] = self.month_start
        context["previous_month"] = shift_month(self.month_start, -1)
        context["next_month"] = shift_month(self.month_start, 1)
        return context

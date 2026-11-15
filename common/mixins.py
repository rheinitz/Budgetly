from typing import Any


class DeleteFormInstanceMixin:
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

from typing import Any

from django import forms


class BootstrapFormMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget_class = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
            current_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{current_class} {widget_class}".strip()


class DisabledFieldsMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

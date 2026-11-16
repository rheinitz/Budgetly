from typing import Any

from django import forms

from categories.models import Type
from common.forms import BootstrapFormMixin, DisabledFieldsMixin


class TypeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Type
        fields = ["category", "name"]
        labels = {
            "category": "Category",
            "name": "Name",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Groceries"}),
        }
        help_texts = {
            "category": "The main category decides how amounts count in the totals.",
            "name": "2-40 characters, unique within its category.",
        }
        error_messages = {
            "category": {
                "required": "Choose a category.",
            },
            "name": {
                "required": "Enter a name.",
                "max_length": "Name cannot be longer than 40 characters.",
            },
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.transactions.exists():
            self.fields["category"].disabled = True
            self.fields["category"].help_text = (
                "Locked because this type already has transactions."
            )


class TypeDeleteForm(DisabledFieldsMixin, TypeForm):
    pass

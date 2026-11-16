from typing import Any

from django import forms

from categories.models import Subcategory
from common.forms import BootstrapFormMixin, DisabledFieldsMixin


class SubcategoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Subcategory
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
        if self.instance.pk and self.instance.entries.exists():
            self.fields["category"].disabled = True
            self.fields["category"].help_text = (
                "Locked because this subcategory already has entries."
            )


class SubcategoryDeleteForm(DisabledFieldsMixin, SubcategoryForm):
    pass

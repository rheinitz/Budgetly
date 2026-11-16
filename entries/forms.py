from django import forms

from common.constants import CURRENCY_SYMBOL
from common.forms import BootstrapFormMixin, DisabledFieldsMixin
from entries.models import Entry


class EntryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["date", "subcategory", "amount", "description", "tags"]
        labels = {
            "date": "Date",
            "subcategory": "Subcategory",
            "amount": f"Amount ({CURRENCY_SYMBOL})",
            "description": "Description",
            "tags": "Tags",
        }
        widgets = {
            "date": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"step": "0.01", "placeholder": "0.00"}),
            "description": forms.TextInput(attrs={"placeholder": "e.g. Market"}),
        }
        help_texts = {
            "amount": "Always positive; the category decides how it counts.",
            "tags": "Optional. Hold Ctrl (Cmd on Mac) to select several.",
        }
        error_messages = {
            "subcategory": {
                "required": "Choose a subcategory.",
            },
            "amount": {
                "required": "Enter an amount.",
                "invalid": "Enter a valid amount.",
                "max_decimal_places": "Amount cannot have more than 2 decimal places.",
                "max_digits": "Amount cannot have more than 10 digits.",
            },
            "date": {
                "required": "Enter a date.",
                "invalid": "Enter a valid date.",
            },
        }


class EntryDeleteForm(DisabledFieldsMixin, EntryForm):
    pass

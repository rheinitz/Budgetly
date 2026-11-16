from django import forms
from django.core.exceptions import ValidationError

from categories.choices import Category
from common.constants import CURRENCY_SYMBOL
from common.forms import BootstrapFormMixin, DisabledFieldsMixin
from transactions.choices import TransactionPageSize, TransactionSort
from transactions.models import Transaction
from tags.models import Tag


class TransactionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "type", "amount", "description", "tags"]
        labels = {
            "date": "Date",
            "type": "Type",
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
            "type": {
                "required": "Choose a type.",
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


class TransactionDeleteForm(DisabledFieldsMixin, TransactionForm):
    pass


class TransactionFilterForm(BootstrapFormMixin, forms.Form):
    q = forms.CharField(
        label="Search",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Description or type"}),
    )
    category = forms.ChoiceField(
        label="Category",
        required=False,
        choices=[("", "All categories"), *Category.choices],
    )
    tag = forms.ModelChoiceField(
        label="Tag",
        required=False,
        queryset=Tag.objects.all(),
        empty_label="All tags",
    )
    start = forms.DateField(
        label="Start",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )
    end = forms.DateField(
        label="End",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )
    sort = forms.ChoiceField(
        label="Sort",
        required=False,
        choices=TransactionSort.choices,
    )
    per_page = forms.TypedChoiceField(
        label="Per page",
        required=False,
        choices=TransactionPageSize.choices,
        coerce=int,
        empty_value=TransactionPageSize.TEN,
    )

    def clean(self) -> dict[str, object]:
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        if start and end and start > end:
            raise ValidationError("Start date must be on or before the end date.")
        return cleaned_data

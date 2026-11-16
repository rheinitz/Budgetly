from django import forms
from django.core.exceptions import ValidationError

from categories.choices import Category
from common.constants import CURRENCY_SYMBOL
from common.forms import BootstrapFormMixin, DisabledFieldsMixin
from entries.choices import EntryPageSize, EntrySort
from entries.models import Entry
from tags.models import Tag


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


class EntryFilterForm(BootstrapFormMixin, forms.Form):
    q = forms.CharField(
        label="Search",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Description or subcategory"}),
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
        choices=EntrySort.choices,
    )
    per_page = forms.TypedChoiceField(
        label="Per page",
        required=False,
        choices=EntryPageSize.choices,
        coerce=int,
        empty_value=EntryPageSize.TEN,
    )

    def clean(self) -> dict[str, object]:
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        if start and end and start > end:
            raise ValidationError("Start date must be on or before the end date.")
        return cleaned_data

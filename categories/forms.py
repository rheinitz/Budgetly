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


class SubcategoryDeleteForm(DisabledFieldsMixin, SubcategoryForm):
    pass

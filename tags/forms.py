from typing import Any

from django import forms
from django.core.validators import RegexValidator

from common.forms import BootstrapFormMixin, DisabledFieldsMixin
from tags.models import Tag


class TagForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name", "color"]
        labels = {
            "name": "Name",
            "color": "Color",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. summer-trip"}),
        }
        help_texts = {
            "name": "Letters, digits and spaces. Saved in lowercase with hyphens.",
            "color": "Color of the tag badge.",
        }
        error_messages = {
            "name": {
                "required": "Enter a name.",
                "max_length": "Name cannot be longer than 30 characters.",
                "unique": "This tag already exists.",
            },
            "color": {
                "required": "Choose a color.",
            },
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].validators = [
            validator
            for validator in self.fields["name"].validators
            if not isinstance(validator, RegexValidator)
        ]

    def clean_name(self) -> str:
        name: str = self.cleaned_data["name"]
        return "-".join(name.lower().split())


class TagDeleteForm(DisabledFieldsMixin, TagForm):
    pass

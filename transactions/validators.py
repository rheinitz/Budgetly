from datetime import date

from django.core.exceptions import ValidationError


def validate_not_in_future(value: date) -> None:
    if value > date.today():
        raise ValidationError("The date cannot be in the future.")

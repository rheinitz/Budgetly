from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.urls import reverse

from common.models import TimeStampMixin
from tags.choices import TagColor


class Tag(TimeStampMixin):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
                message='Use lowercase letters, digits and single hyphens, e.g. "summer-trip".',
            ),
        ],
    )
    color = models.CharField(
        max_length=20,
        choices=TagColor.choices,
        default=TagColor.SECONDARY,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("tags:detail", kwargs={"pk": self.pk})

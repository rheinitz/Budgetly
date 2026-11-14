from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

from categories.choices import Category
from common.models import TimeStampMixin


class Subcategory(TimeStampMixin):
    category = models.CharField(max_length=20, choices=Category.choices)
    name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2, message="Name must be at least 2 characters."),
        ],
    )

    class Meta:
        ordering = ["category", "name"]
        unique_together = [("category", "name")]
        verbose_name_plural = "subcategories"

    def __str__(self) -> str:
        return f"{self.get_category_display()} - {self.name}"

    def clean(self) -> None:
        super().clean()
        if not self.category or not self.name:
            return

        lowered_name = self.name.lower()
        others = Subcategory.objects.filter(category=self.category).exclude(pk=self.pk)
        if any(other.name.lower() == lowered_name for other in others):
            raise ValidationError(
                {
                    "name": (
                        "A subcategory with this name already exists in "
                        f"{self.get_category_display()}."
                    ),
                }
            )

    @property
    def category_choice(self) -> Category:
        return Category(self.category)

    def get_absolute_url(self) -> str:
        return reverse("categories:detail", kwargs={"pk": self.pk})

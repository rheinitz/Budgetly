from datetime import date
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from categories.choices import Category
from common.models import TimeStampMixin
from entries.querysets import EntryQuerySet
from entries.validators import validate_not_in_future


class Entry(TimeStampMixin):
    subcategory = models.ForeignKey(
        "categories.Subcategory",
        on_delete=models.RESTRICT,
        related_name="entries",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        related_name="entries",
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    description = models.CharField(max_length=200, blank=True, default="")
    date = models.DateField(
        default=date.today,
        validators=[validate_not_in_future],
        db_index=True,
    )

    objects = EntryQuerySet.as_manager()

    class Meta:
        ordering = ["-date", "-created_at"]
        verbose_name_plural = "entries"

    def __str__(self) -> str:
        return f"{self.date:%Y-%m-%d} - {self.subcategory.name} - {self.amount:.2f}"

    @property
    def category(self) -> Category:
        return self.subcategory.category_choice

    def get_month_url(self) -> str:
        return reverse(
            "entries:month",
            kwargs={"year": self.date.year, "month": self.date.month},
        )

    def get_absolute_url(self) -> str:
        return reverse("entries:detail", kwargs={"pk": self.pk})

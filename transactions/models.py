from datetime import date
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from categories.choices import Category
from common.models import TimeStampMixin
from transactions.querysets import TransactionQuerySet
from transactions.validators import validate_not_in_future


class Transaction(TimeStampMixin):
    type = models.ForeignKey(
        "categories.Type",
        on_delete=models.RESTRICT,
        related_name="transactions",
    )
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        related_name="transactions",
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

    objects = TransactionQuerySet.as_manager()

    class Meta:
        ordering = ["-date", "-created_at"]
        verbose_name = "transaction"
        verbose_name_plural = "transactions"

    def __str__(self) -> str:
        return f"{self.date:%Y-%m-%d} - {self.type.name} - {self.amount:.2f}"

    @property
    def category(self) -> Category:
        return self.type.category_choice

    def get_month_url(self) -> str:
        return reverse(
            "transactions:month",
            kwargs={"year": self.date.year, "month": self.date.month},
        )

    def get_absolute_url(self) -> str:
        return reverse("transactions:detail", kwargs={"pk": self.pk})

from datetime import date
from decimal import Decimal
from typing import Self

from django.db import models
from django.db.models import Q, Sum

from categories.choices import Category
from entries.totals import CategoryTotals
from tags.models import Tag


class EntryQuerySet(models.QuerySet):
    def for_month(self, year: int, month: int) -> Self:
        return self.filter(date__year=year, date__month=month)

    def with_related(self) -> Self:
        return self.select_related("subcategory").prefetch_related("tags")

    def search(self, text: str) -> Self:
        if not text:
            return self
        return self.filter(
            Q(description__icontains=text) | Q(subcategory__name__icontains=text)
        )

    def in_category(self, category: str) -> Self:
        if not category:
            return self
        return self.filter(subcategory__category=category)

    def with_tag(self, tag: Tag | None) -> Self:
        if not tag:
            return self
        return self.filter(tags=tag)

    def between(self, start: date | None, end: date | None) -> Self:
        if start:
            self = self.filter(date__gte=start)
        if end:
            self = self.filter(date__lte=end)
        return self

    def totals_by_category(self) -> dict[str, Decimal]:
        grouped = (
            self.order_by()
            .values("subcategory__category")
            .annotate(total=Sum("amount"))
        )
        totals = {category.value: Decimal("0.00") for category in Category}
        for row in grouped:
            totals[row["subcategory__category"]] = row["total"]
        return totals

    def totals(self) -> CategoryTotals:
        return CategoryTotals(self.totals_by_category())

    def total_amount(self) -> Decimal:
        total = self.aggregate(Sum("amount"))["amount__sum"]
        if total is None:
            return Decimal("0.00")
        return total

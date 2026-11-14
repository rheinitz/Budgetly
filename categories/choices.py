from django.db import models


class Category(models.TextChoices):
    INCOME = "income"
    EXPENSE = "expense"
    SAVINGS = "savings"
    INVESTMENTS = "investments"

    @property
    def badge_color(self) -> str:
        colors = {
            Category.INCOME: "success",
            Category.EXPENSE: "danger",
            Category.SAVINGS: "primary",
            Category.INVESTMENTS: "info",
        }
        return colors[self]

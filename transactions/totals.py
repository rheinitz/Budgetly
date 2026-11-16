from decimal import Decimal

from categories.choices import Category


class CategoryTotals:
    def __init__(self, amounts: dict[str, Decimal]) -> None:
        self._amounts = amounts

    @property
    def income(self) -> Decimal:
        return self._amounts[Category.INCOME]

    @property
    def expenses(self) -> Decimal:
        return self._amounts[Category.EXPENSE]

    @property
    def savings(self) -> Decimal:
        return self._amounts[Category.SAVINGS]

    @property
    def investments(self) -> Decimal:
        return self._amounts[Category.INVESTMENTS]

    @property
    def net(self) -> Decimal:
        return self.income - self.expenses - self.savings - self.investments

    @property
    def savings_rate(self) -> Decimal | None:
        if self.income == 0:
            return None
        rate = (self.savings + self.investments) / self.income * 100
        return rate.quantize(Decimal("0.1"))

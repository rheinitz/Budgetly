from datetime import date

from django.http import Http404


def get_month_start_or_404(year: int, month: int) -> date:
    try:
        return date(year, month, 1)
    except ValueError:
        raise Http404("Invalid month.")


def shift_month(month_start: date, months: int) -> date:
    month_index = month_start.month - 1 + months
    year = month_start.year + month_index // 12
    month = month_index % 12 + 1
    return date(year, month, 1)

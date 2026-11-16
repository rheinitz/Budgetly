from decimal import Decimal, InvalidOperation

from django import template

from common.constants import CURRENCY_SYMBOL

register = template.Library()


@register.filter
def money(value: object) -> str:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, TypeError):
        return ""
    return f"{amount:,.2f} {CURRENCY_SYMBOL}"


@register.inclusion_tag("partials/totals_cards.html")
def totals_cards(totals: object) -> dict[str, object]:
    return {"totals": totals}

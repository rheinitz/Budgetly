from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["date", "type", "amount"]
    list_filter = ["type__category", "tags"]
    ordering = ["-date", "-created_at"]
    list_select_related = ["type"]

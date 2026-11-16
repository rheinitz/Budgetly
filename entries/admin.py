from django.contrib import admin

from entries.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["date", "subcategory", "amount"]
    list_filter = ["subcategory__category", "tags"]
    ordering = ["-date", "-created_at"]
    list_select_related = ["subcategory"]

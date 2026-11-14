from django.contrib import admin

from categories.models import Subcategory


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at"]
    list_filter = ["category"]
    ordering = ["category", "name"]

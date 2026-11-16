from django.contrib import admin

from categories.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "created_at"]
    list_filter = ["category"]
    ordering = ["category", "name"]

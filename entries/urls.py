from django.urls import path

from entries.views import (
    EntryCreateView,
    EntryDeleteView,
    EntryDetailView,
    EntryUpdateView,
    MonthEntriesView,
    current_month,
)

app_name = "entries"

urlpatterns = [
    path("current/", current_month, name="current"),
    path("add/", EntryCreateView.as_view(), name="add"),
    path("<int:year>/<int:month>/", MonthEntriesView.as_view(), name="month"),
    path("<int:pk>/", EntryDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", EntryUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", EntryDeleteView.as_view(), name="delete"),
]

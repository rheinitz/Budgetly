from django.urls import path

from entries.views import MonthEntriesView, current_month

app_name = "entries"

urlpatterns = [
    path("current/", current_month, name="current"),
    path("<int:year>/<int:month>/", MonthEntriesView.as_view(), name="month"),
]

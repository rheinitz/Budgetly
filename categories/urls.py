from django.urls import path

from categories.views import (
    TypeCreateView,
    TypeDeleteView,
    TypeDetailView,
    TypeListView,
    TypeUpdateView,
)

app_name = "types"

urlpatterns = [
    path("", TypeListView.as_view(), name="list"),
    path("add/", TypeCreateView.as_view(), name="add"),
    path("<int:pk>/", TypeDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", TypeUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", TypeDeleteView.as_view(), name="delete"),
]

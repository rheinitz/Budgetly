from django.urls import path

from categories.views import (
    SubcategoryCreateView,
    SubcategoryDeleteView,
    SubcategoryDetailView,
    SubcategoryListView,
    SubcategoryUpdateView,
)

app_name = "categories"

urlpatterns = [
    path("", SubcategoryListView.as_view(), name="list"),
    path("add/", SubcategoryCreateView.as_view(), name="add"),
    path("<int:pk>/", SubcategoryDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", SubcategoryUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", SubcategoryDeleteView.as_view(), name="delete"),
]

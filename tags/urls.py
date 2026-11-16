from django.urls import path

from tags.views import (
    TagCreateView,
    TagDeleteView,
    TagDetailView,
    TagListView,
    TagUpdateView,
)

app_name = "tags"

urlpatterns = [
    path("", TagListView.as_view(), name="list"),
    path("add/", TagCreateView.as_view(), name="add"),
    path("<int:pk>/", TagDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", TagUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", TagDeleteView.as_view(), name="delete"),
]

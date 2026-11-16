from django.urls import path

from transactions.views import (
    TransactionCreateView,
    TransactionDeleteView,
    TransactionDetailView,
    TransactionListView,
    TransactionUpdateView,
    MonthTransactionsView,
    current_month,
)

app_name = "transactions"

urlpatterns = [
    path("", TransactionListView.as_view(), name="list"),
    path("current/", current_month, name="current"),
    path("add/", TransactionCreateView.as_view(), name="add"),
    path("<int:year>/<int:month>/", MonthTransactionsView.as_view(), name="month"),
    path("<int:pk>/", TransactionDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", TransactionUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", TransactionDeleteView.as_view(), name="delete"),
]

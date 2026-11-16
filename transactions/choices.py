from django.db import models


class TransactionPageSize(models.IntegerChoices):
    TEN = 10, "10"
    TWENTY = 20, "20"
    FIFTY = 50, "50"
    ONE_HUNDRED = 100, "100"


class TransactionSort(models.TextChoices):
    NEWEST = "-date", "Newest first"
    OLDEST = "date", "Oldest first"
    LARGEST = "-amount", "Largest amount"
    SMALLEST = "amount", "Smallest amount"

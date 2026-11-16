from django.db import models


class TagColor(models.TextChoices):
    PRIMARY = "primary", "Primary"
    SECONDARY = "secondary", "Secondary"
    SUCCESS = "success", "Success"
    DANGER = "danger", "Danger"
    WARNING = "warning", "Warning"
    INFO = "info", "Info"
    DARK = "dark", "Dark"

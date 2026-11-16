from django.urls import path

from common.views import AboutView, HomeView, set_theme

app_name = "common"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("theme/<str:theme>/", set_theme, name="theme"),
]

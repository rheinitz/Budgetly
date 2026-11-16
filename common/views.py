from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import TemplateView

from common.constants import THEME_COOKIE, THEMES

THEME_COOKIE_MAX_AGE = 365 * 24 * 60 * 60


class HomeView(TemplateView):
    template_name = "common/home.html"


class AboutView(TemplateView):
    template_name = "common/about.html"


def set_theme(request: HttpRequest, theme: str) -> HttpResponseRedirect:
    if theme not in THEMES:
        raise Http404("Unknown theme.")

    next_url = request.GET.get("next", "")
    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = reverse("common:home")

    response = redirect(next_url)
    response.set_cookie(THEME_COOKIE, theme, max_age=THEME_COOKIE_MAX_AGE, samesite="Lax")
    return response

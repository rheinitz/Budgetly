from django.http import HttpRequest

from common.constants import DEFAULT_THEME, THEME_COOKIE, THEMES


def theme(request: HttpRequest) -> dict[str, str]:
    current = request.COOKIES.get(THEME_COOKIE, DEFAULT_THEME)
    if current not in THEMES:
        current = DEFAULT_THEME
    other = "light" if current == "dark" else "dark"
    return {"theme": current, "other_theme": other}

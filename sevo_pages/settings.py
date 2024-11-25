from django.conf import settings


SEVO_PAGES_MENU_MAIN = "Main"
SEVO_PAGES_MENU_META = "Meta"

if hasattr(settings, "SEVO_PAGES_MENU_MAIN"):
    SEVO_PAGES_MENU_MAIN = settings.SEVO_PAGES_MENU_MAIN

if hasattr(settings, "SEVO_PAGES_MENU_META"):
    SEVO_PAGES_MENU_META = settings.SEVO_PAGES_MENU_META
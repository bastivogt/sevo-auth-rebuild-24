from django.conf import settings


SEVO_MAINTAINANCE = False

if hasattr(settings, "SEVO_MAINTAINANCE"):
    SEVO_MAINTAINANCE = settings.SEVO_MAINTAINANCE
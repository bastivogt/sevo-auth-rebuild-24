from django.conf import settings


# defaults
SEVO_AUTH_CAN_SIGN_UP = True
SEVO_AUTH_REDIRECT_IF_CANT_SIGN_UP = "sevo-auth-index"
SEVO_AUTH_REDIRECT_AFTER_SIGN_UP = "sevo-auth-index"
SEVO_AUTH_REDIRECT_AFTER_SIGN_IN = "sevo-auth-index"
SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT = "sevo-auth-index"
SEVO_AUTH_FROM_EMAIL = "sevo.auth@sevo.de"

if hasattr(settings, "SEVO_AUTH_CAN_SIGN_UP"):
    SEVO_AUTH_CAN_SIGN_UP = settings.SEVO_AUTH_CAN_SIGN_UP


if hasattr(settings, "SEVO_AUTH_REDIRECT_IF_CANT_SIGN_UP"):
    SEVO_AUTH_REDIRECT_IF_CANT_SIGN_UP = settings.SEVO_AUTH_REDIRECT_IF_CANT_SIGN_UP
    

if hasattr(settings, "SEVO_AUTH_REDIRECT_AFTER_SIGN_IN"):
    SEVO_AUTH_REDIRECT_AFTER_SIGN_IN = settings.SEVO_AUTH_REDIRECT_AFTER_SIGN_IN


if hasattr(settings, "SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT"):
    SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT = settings.SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT


if hasattr(settings, "SEVO_AUTH_FROM_EMAIL"):
    SEVO_AUTH_FROM_EMAIL = settings.SEVO_AUTH_FROM_EMAIL

print("SEVO_AUTH_CAN_SIGN_UP:", SEVO_AUTH_CAN_SIGN_UP)
print("SEVO_AUTH_REDIRECT_AFTER_SIGN_IN:", SEVO_AUTH_REDIRECT_AFTER_SIGN_IN)
print("SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT:", SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT)
print("SEVO_AUTH_FROM_EMAIL:", SEVO_AUTH_FROM_EMAIL)




from django.contrib import admin

from .models import PasswordResetToken

# Register your models here.

class PasswordResetTokenAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "token",
        "done",
        "created_at"
    ]

    list_filter = [
        "user",
        "done",
        "created_at"
    ]



admin.site.register(PasswordResetToken, PasswordResetTokenAdmin)
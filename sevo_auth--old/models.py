from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"user: {self.user}, token: {self.token}"
    

    class Meta:
        verbose_name = "Password Reset Token"
        verbose_name_plural = "Password Reset Tokens"
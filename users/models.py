from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    password1 = models.CharField(_('password'), max_length=128, blank=True)

    def __str__(self):
        return self.email

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    telegram_id = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"{self.username} id:{self.id}"


from django.db import models
from django.contrib.auth.models import User

class PasswordSaver(models.Model):
    username = models.CharField(max_length=255, unique=True)
    app_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username

    def Meta():
        pass
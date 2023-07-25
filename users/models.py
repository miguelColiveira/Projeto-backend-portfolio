from django.db import models
from django.contrib.auth.models import AbstractUser


class UserChoices(models.TextChoices):
    STUDENT = ("student",)
    COLLABORATOR = ("collaborator",)


class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    user_status = models.CharField(
        max_length=20,
        null=True,
        choices=UserChoices.choices,
        default=UserChoices.STUDENT,
    )

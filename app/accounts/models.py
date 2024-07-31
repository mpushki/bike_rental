from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager


class Account(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()

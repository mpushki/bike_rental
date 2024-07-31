from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from accounts.managers import UserManager

class Account(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]


    def __str__(self):
        return self.email

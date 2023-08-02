from django.contrib.auth.hashers import is_password_usable, make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True, null=True, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    def save(self, *args, **kwargs):
        if self.pk is None or not is_password_usable(self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

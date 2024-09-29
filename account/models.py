from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
import random

    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValidationError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError("Superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValidationError("Superuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)

class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    is_verified = models.BooleanField(default=False)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    username = None


class Otp(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(db_index=True)

    def save(self, *args, **kwargs):
        if not self.otp_code:
            self.otp_code = f'{random.randint(100000, 999999)}'
            self.expires_at = timezone.now() + timezone.timedelta(minutes=10)

            super().save(*args, **kwargs)
    
    def is_valid(self):
        return timezone.now() <= self.expires_at


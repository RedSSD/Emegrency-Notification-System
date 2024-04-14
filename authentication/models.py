from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'fullname',
        'phone_number'
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

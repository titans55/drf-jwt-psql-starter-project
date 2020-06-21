from django.db import models as models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, user_type, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_type):
        user = self.create_user(email, password=password, user_type=user_type)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


USER_TYPES = (
    (1, "admin"),
    (2, "service_provider"),
    (3, "customer"),
)


class User(AbstractUser):

    # Fields
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_type = models.IntegerField(choices=USER_TYPES, default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    objects = UserManager()

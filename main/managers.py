from django.conf import settings
from django.utils import timezone
from django.db import models, transaction
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User MUST have an Email! Please Provide An Email...')

        staff_email = self.normalize_email(email)
        user = self.model(email=staff_email, **extra_fields)
        user.is_banned = False

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.staff = True
        user.admin = True
        user.position = 'admin'
        user.save(using=self._db)
        return user

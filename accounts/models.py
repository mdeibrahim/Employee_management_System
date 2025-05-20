from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager # Import the manager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # Set to True by default, can be False for email verification
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email' # Use email for login [cite: 5]
    REQUIRED_FIELDS = [] # No other fields required besides email and password by default

    objects = CustomUserManager() # Attach the custom manager

    def __str__(self):
        return self.email
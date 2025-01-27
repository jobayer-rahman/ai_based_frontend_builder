from django.db import models
from .utils import UserManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(default=)
    # updated_at = models.DateTimeField()
    # last_login = models.DateTimeField()
    
    objects = UserManager()
    
    USERNAME_FIELD = None
    REQUIRED_FIELDS = ['username', 'email']
    
    def __str__(self):
        return self.username
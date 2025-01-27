from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required.")
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)
    
    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(username, email, first_name, last_name, password, **extra_fields) 
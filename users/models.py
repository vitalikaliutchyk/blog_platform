from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('user', 'Автор'),
        ('moderator', 'Модератор'),
        ('admin', 'Админ'),
    )
    role = models.CharField(max_length=15, choices=ROLES, default='user')
    bio = models.TextField(blank=True)

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, blank=True)
    bio = models.TextField(blank=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',  # Custom related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Custom related_name
        related_query_name='user',
    )

    class Meta:
        app_label = 'accounts'

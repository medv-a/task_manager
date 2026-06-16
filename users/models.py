from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MANAGER = 'manager', 'Менеджер'
        USER = 'user', 'Пользователь'

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name="Уровень доступа"
    )

    bio = models.TextField(max_length=500, blank=True, verbose_name="О себе")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

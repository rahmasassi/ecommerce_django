from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    ROLES=(
        ('user','user'),
        ('admin','admin')
    )

    #unique email
    email=models.EmailField(unique=True)

    role=models.CharField(max_length=30,choices=ROLES,default='user')

    description=models.TextField(blank=True, default='')

    def __str__(self):
        return self.username



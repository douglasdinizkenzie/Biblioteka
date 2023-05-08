from django.db import models
from django.contrib.auth.models import AbstractUser
from copies.models import Copy


class User(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_student = models.BooleanField(null=True, default=True)
    is_collaborator = models.BooleanField(null=True, default=False)
    is_blocked = models.BooleanField(default=False)
    blocked_until = models.DateTimeField(blank=True, null=True)
    loans = models.ManyToManyField(
        Copy, through="copies.Book_loans", related_name="users"
    )

    def __str__(self):
        return self.username

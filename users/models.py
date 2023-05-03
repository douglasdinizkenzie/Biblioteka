from django.db import models
from django.contrib.auth.models import AbstractUser
from copies.models import Copies


class User(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_stundent = models.BooleanField(null=True, default=True)
    is_collaborator = models.BooleanField(null=True, default=False)
    is_blocked = models.BooleanField(default=False)
    copies = models.ManyToManyField(Copies, through="copies.Book_loans", related_name="users")

    def __str__(self):
        return self.username

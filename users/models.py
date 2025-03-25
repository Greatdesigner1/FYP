from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(AbstractUser, TimeStamp):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(unique=True)

    def __str__(self):
        return self.username
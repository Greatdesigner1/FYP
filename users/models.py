from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


GENDERS = {
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
}

LEVEL = {
    ("100", "100L"),
    ("200", "200L"),
    ("300", "300L"),
    ("400", "400L"),
    ("500", "500L")
}


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

from django.db import models
from django.db.models.base import Model

from apps.utils.models import Timestamps


class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist entries'

from django.db import models
from django.db.models.base import Model
from apps.utils.models import Timestamps


class Certificates(Timestamps, models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

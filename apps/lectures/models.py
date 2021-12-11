from django.db import models


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text="Enter number of hours")
    slides_url = models.CharField(max_length=255)
    is_required = models.BooleanField(default=True)

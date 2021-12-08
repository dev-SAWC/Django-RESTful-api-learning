from django.db import models
from django.db.models.fields import EmailField

from apps.utils.models import Timestamps

# Create your models here.
class WaitlistEntry(Timestamps,models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name = "Email Address",
        max_length = 255,
        unique = True,
    )
    notes = models.TextField()

    class Meta:
        verbose_name_plural = "Waitlist Entries"


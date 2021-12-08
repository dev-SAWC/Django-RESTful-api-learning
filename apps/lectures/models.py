from django.db import models
from django.db.models.fields import EmailField

from apps.utils.models import Timestamps

# Create your models here.
class Lecture(Timestamps,models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    slides_url = models.CharField(max_length=255)


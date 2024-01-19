# mobi_app/models/exercise.py

from django.db import models
from django.conf import settings

class Exercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='exercises')
    name = models.CharField(max_length=255)
    description = models.TextField()
    # TODO: type should be a drop list to have restricted options
    type = models.CharField(max_length=255)

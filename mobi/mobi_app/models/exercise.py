# mobi_app/models/exercise.py

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # TODO: type should be a drop list to have restricted options
    type = models.CharField(max_length=255)

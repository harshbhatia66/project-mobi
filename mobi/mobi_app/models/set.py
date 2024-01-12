# mobi_app/models/set.py

from django.db import models
from .session_exercise import SessionExercise

class Set(models.Model):
    session_exercise = models.ForeignKey(SessionExercise, on_delete=models.CASCADE, related_name='sets')
    reps = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)  # Duration in seconds
    notes = models.TextField(blank=True, null=True)

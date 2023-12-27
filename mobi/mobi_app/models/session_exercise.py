# mobi_app/models/session_exercise.py

from django.db import models
from .workout_session import WorkoutSession
from .exercise import Exercise

class SessionExercise(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE, related_name='session_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='session_exercises')

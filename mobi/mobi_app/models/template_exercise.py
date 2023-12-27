# mobi_app/models/template_exercise.py

from django.db import models
from .workout_template import WorkoutTemplate
from .exercise import Exercise

class TemplateExercise(models.Model):
    workout_template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='template_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
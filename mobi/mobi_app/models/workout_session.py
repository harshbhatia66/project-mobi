# mobi_app/models/workout_session.py

from django.db import models
from .workout_template import WorkoutTemplate
from django.conf import settings
class WorkoutSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_sessions')
    workout_template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='workout_sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

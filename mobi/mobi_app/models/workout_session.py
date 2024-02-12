# mobi_app/models/workout_session.py

from django.db import models
from .workout_template import WorkoutTemplate
from django.conf import settings
class WorkoutSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_sessions')
    workout_template = models.ForeignKey(WorkoutTemplate, on_delete=models.SET_NULL, related_name='workout_sessions', null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    # TODO: Check if this right
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.get_name_based_on_template_or_time()
        super().save(*args, **kwargs)

    def get_name_based_on_template_or_time(self):
        if self.workout_template:
            return self.workout_template.name

        hour = self.start_time.hour
        if 5 <= hour < 12:
            return "Morning Workout"
        elif 12 <= hour < 17:
            return "Afternoon Workout"
        else:
            return "Night Workout"

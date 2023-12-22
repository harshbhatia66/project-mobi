# mobi_app/models/workout_template.py

from django.db import models
from django.conf import settings

class WorkoutTemplate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout_templates') 
    # Creates a foreign key relationship to the user model. Establishes a many to one relationship from Workout Template to User.
    # This means that each WorkoutTemplate is associated with one user, but each User can have multiple WorkoutTemplates.
    # On delete specifies what happens when the reference user is deleted -> cascade means delete all associated workout templates if the User is deleted.
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
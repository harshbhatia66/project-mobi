from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

class Exercise(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='exercises'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, help_text=_("Type of exercise, e.g., cardio, strength."))
    function = models.CharField(max_length=255, blank=True, help_text=_("Functional focus of the exercise, e.g., 'Chest', 'Legs'."))
    equipment_type = models.CharField(max_length=255, blank=True, help_text=_("Type of equipment used, e.g., 'Dumbbell', 'Machine'."))
    image = models.ImageField(upload_to='media/exercise_images/', blank=True, null=True)
    gif = models.FileField(upload_to='media/exercise_gifs/', blank=True, null=True)
    instructions = models.TextField(blank=True)

    # JSON fields to store structured data
    history = models.JSONField(blank=True, null=True)
    # charts = models.JSONField(blank=True, null=True)
    # personal_records = models.JSONField(blank=True, null=True)

    def clean(self):
        # Ensure that an exercise has either an image or a gif, not both
        if self.image and self.gif:
            raise ValidationError(_('An exercise cannot have both an image and a gif. Please choose one.'))
        
        # Check if the exercise name exists globally (assuming global exercises have user=None)
        if Exercise.objects.filter(Q(user__isnull=True) | Q(user=self.user), name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': _('An exercise with this name already exists.')})

    def save(self, *args, **kwargs):
        self.full_clean()  # Call the clean method to perform the custom validation
        super().save(*args, **kwargs)
    
    def update_history(self):
        # Start with an empty list for the history data
        history = []

        # Get all session exercises for this exercise
        session_exercises = self.session_exercises.all().prefetch_related('sets')

        # Iterate through each session exercise to build the history
        for session_exercise in session_exercises:
            session = session_exercise.workout_session
            sets = session_exercise.sets.all()
            
            session_data = {
                "session_date": session.start_time,
                "workout_name": session.name,
                "sets": [{"reps": s.reps, "weight": s.weight} for s in sets],
                # Add any additional aggregate data 
                # "total_volume": sum(s.reps * s.weight for s in sets if s.reps and s.weight),
                # "1RM": max(calculate_1rm(s.weight, s.reps) for s in sets if s.reps and s.weight)  # Assuming a calculate_1rm function exists
            }
            history.append(session_data)

        # Save the history data as a JSON string in the history_data field
        self.history = history
        self.save()

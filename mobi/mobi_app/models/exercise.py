from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

class Exercise(models.Model):
    TYPE_CHOICES = [
        ('Strength', 'Strength'),
        ('Cardio', 'Cardio'),
        ('Flexibility', 'Flexibility'), 
        ('Balance', 'Balance'),          
    ]
    FUNCTION_CHOICES = [
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Biceps', 'Biceps'),
        ('Triceps', 'Triceps'),
        ('Forearms', 'Forearms'),
        ('Abs', 'Abs'),
        ('Quadriceps', 'Quadriceps'),
        ('Hamstrings', 'Hamstrings'),
        ('Calves', 'Calves'),
        ('Shoulders', 'Shoulders'),
        ('Full Body', 'Full Body'),
    ]
    EQUIPMENT_TYPE_CHOICES = [
        ('Barbell', 'Barbell'),
        ('Dumbbell', 'Dumbbell'),
        ('Machine', 'Machine'),
        ('Weighted Bodyweight', 'Weighted Bodyweight'),
        ('Assisted Bodyweight', 'Assisted Bodyweight'),
        ('Reps Only', 'Reps Only'),
        ('Duration', 'Duration'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='exercises'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        help_text=_("Type of exercise, e.g., cardio, strength.")
    )
    function = models.CharField(
        max_length=50,
        choices=FUNCTION_CHOICES,
        blank=True,
        help_text=_("Functional focus of the exercise, e.g., 'Chest', 'Legs'.")
    )
    equipment_type = models.CharField(
        max_length=50,
        choices=EQUIPMENT_TYPE_CHOICES,
        blank=True,
        help_text=_("Type of equipment used, e.g., 'Dumbbell', 'Machine'.")
    )
    image = models.ImageField(upload_to='media/exercise_images/', blank=True, null=True)
    gif = models.FileField(upload_to='media/exercise_gifs/', blank=True, null=True)
    instructions = models.JSONField(blank=True, default=list)

    history = models.JSONField(blank=True, null=True)

    def clean(self):
        # Check if the exercise name exists globally (assuming global exercises have user=None)
        if Exercise.objects.filter(Q(user__isnull=True) | Q(user=self.user), name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': _('An exercise with this name already exists.')})

    def save(self, *args, **kwargs):
        self.full_clean()  # Call the clean method to perform the custom validation
        super().save(*args, **kwargs)
    
    def update_history(self):
        # Implementation remains the same
        pass

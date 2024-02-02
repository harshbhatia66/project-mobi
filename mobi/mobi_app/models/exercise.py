# mobi_app/models/exercise.py

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
class Exercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='exercises')
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)  # TODO: type should be a drop list to have restricted options
    # muscle group swtich with type

    def clean(self):
        # Check if the exercise name exists globally (assuming global exercises have user=None)
        if Exercise.objects.filter(Q(user__isnull=True) | Q(user=self.user), name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'An exercise with this name already exists.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Call the clean method to perform the custom validation
        super().save(*args, **kwargs)

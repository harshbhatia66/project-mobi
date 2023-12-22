# mobi_app/models/user_progress.py

from django.db import models
from django.conf import settings
class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_progress')
    date = models.DateTimeField()
    metric = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)

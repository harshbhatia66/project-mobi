# mobi_app/forms.py

from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'type', 'function', 'equipment_type', 'image', 'gif', 'instructions', 'user']

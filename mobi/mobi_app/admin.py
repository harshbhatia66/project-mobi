from django.contrib import admin
from .models import (
    Exercise,
    WorkoutTemplate,
    TemplateExercise,
    WorkoutSession,
    SessionExercise,
    Set,
    UserProgress
)

admin.site.register(Exercise)
admin.site.register(SessionExercise)
admin.site.register(Set)
admin.site.register(TemplateExercise)
admin.site.register(UserProgress)
admin.site.register(WorkoutSession)
admin.site.register(WorkoutTemplate)


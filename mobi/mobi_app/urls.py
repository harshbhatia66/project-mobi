from django.urls import path
from .views import (UserList, UserDetail, ExerciseList, ExerciseDetail, 
                    WorkoutTemplateList, WorkoutTemplateDetail, 
                    TemplateExerciseList, TemplateExerciseDetail, 
                    WorkoutSessionList, WorkoutSessionDetail, 
                    SessionExerciseList, SessionExerciseDetail, 
                    SetList, SetDetail, UserProgressDetail)
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # User URLs
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Exercise URLs
    path('exercises/', ExerciseList.as_view(), name='exercise-list'),
    path('exercises/<int:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),

    # Workout Template URLs
    path('workout_templates/', WorkoutTemplateList.as_view(), name='workouttemplate-list'),
    path('workout_templates/<int:pk>/', WorkoutTemplateDetail.as_view(), name='workouttemplate-detail'),

    # Template Exercise URLs
    path('template_exercises/', TemplateExerciseList.as_view(), name='templateexercise-list'),
    path('template_exercises/<int:pk>/', TemplateExerciseDetail.as_view(), name='templateexercise-detail'),

    # Workout Session URLs
    path('workout_sessions/', WorkoutSessionList.as_view(), name='workoutsession-list'),
    path('workout_sessions/<int:pk>/', WorkoutSessionDetail.as_view(), name='workoutsession-detail'),

    # Session Exercise URLs
    path('session_exercises/', SessionExerciseList.as_view(), name='sessionexercise-list'),
    path('session_exercises/<int:pk>/', SessionExerciseDetail.as_view(), name='sessionexercise-detail'),

    # Set URLs
    path('sets/', SetList.as_view(), name='set-list'),
    path('sets/<int:pk>/', SetDetail.as_view(), name='set-detail'),

    # User Progress URLs
    path('user_progress/', UserProgressDetail.as_view(), name='userprogress-detail'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

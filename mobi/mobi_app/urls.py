from django.urls import path, include
from .views import (UserList, UserDetail, ExerciseList, ExerciseDetail, 
                    WorkoutTemplateList, WorkoutTemplateDetail,
                    WorkoutSessionList, WorkoutSessionDetail, 
                    SessionExerciseList, SessionExerciseDetail, 
                    SetList, SetDetail, UserProgressDetail,
                    TestToken)
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

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

    # Workout Session URLs
    path('workout_sessions/', WorkoutSessionList.as_view(), name='workoutsession-list'),
    path('workout_sessions/<int:pk>/', WorkoutSessionDetail.as_view(), name='workoutsession-detail'),

    # Session Exercise URLs
    path('workout_sessions/<int:workout_session_id>/session_exercises/', SessionExerciseList.as_view(), name='sessionexercise-list'),
    path('session_exercises/<int:session_exercise_id>/', SessionExerciseDetail.as_view(), name='sessionexercise-detail'),

    # Set URLs
    path('session_exercises/<int:session_exercise_id>/sets/', SetList.as_view(), name='set-list'),
    path('sets/<int:set_id>/', SetDetail.as_view(), name='set-detail'),

    # User Progress URLs
    path('user_progress/', UserProgressDetail.as_view(), name='userprogress-detail'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('test-token/', TestToken.as_view(), name='test-token'),
] 

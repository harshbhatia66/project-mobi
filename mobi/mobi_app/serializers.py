# serializers.py

from rest_framework import serializers
from .models import Exercise, WorkoutTemplate, TemplateExercise, WorkoutSession, SessionExercise, Set, UserProgress
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'
        
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class SessionExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    sets = SetSerializer(many=True)

    class Meta:
        model = SessionExercise
        fields = ['id', 'session', 'exercise', 'sets']

class WorkoutSessionSerializer(serializers.ModelSerializer):
    session_exercises = SessionExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = ['id', 'user', 'workout_template', 'start_time', 'end_time', 'notes', 'session_exercises']

class TemplateExerciseSerializer(serializers.ModelSerializer):
    # Include related exercise details
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = TemplateExercise
        fields = ['id', 'workout_template', 'exercise']

class WorkoutTemplateSerializer(serializers.ModelSerializer):
    template_exercises = TemplateExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutTemplate
        fields = ['id', 'user', 'name', 'description', 'template_exercises']

class UserReadSerializer(serializers.ModelSerializer):
    workout_sessions = WorkoutSessionSerializer(many=True, read_only=True)
    user_progress = UserProgressSerializer(many=True, read_only=True)
    workout_templates = WorkoutTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'workout_sessions', 'user_progress', 'workout_templates']

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return User.objects.create(**validated_data)
    







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

    # validate_<field_name> is a method that is called when the serializer is validated
    # In this case name is the field name and this method is called and our function is defined
    # To capitalize each word in the name

    def validate_name(self, value):
        # Capitalize each word in the name
        value = value.title()
        return value

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

class WorkoutTemplateReadSerializer(serializers.ModelSerializer):
    template_exercises = TemplateExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutTemplate
        fields = ['id', 'user', 'name', 'description', 'created_at', 'template_exercises']


class WorkoutTemplateWriteSerializer(serializers.ModelSerializer):
    exercise_ids = serializers.ListField(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = WorkoutTemplate
        fields = ['id', 'name', 'description', 'exercise_ids']

    def create(self, validated_data):
        # Remove 'exercise_ids' from the validated_data and store it in exercise_ids
        exercise_ids = validated_data.pop('exercise_ids')

        # Create a new WorkoutTemplate object using the remaining data in validated_data
        # The ** operator is used to unpack the dictionary into keyword arguments
        workout_template = WorkoutTemplate.objects.create(**validated_data)

        # Loop over each id in exercise_ids
        for exercise_id in exercise_ids:
            # For each id, create a new TemplateExercise object
            # The workout_template is set to the WorkoutTemplate object created above
            # The exercise_id is set to the current id
            # workout_template field is a ForeignKey field in the TemplateExercise model
            # Which means its a reference to a WorkoutTemplate object and we are associating it. 
            TemplateExercise.objects.create(workout_template=workout_template, exercise_id=exercise_id)

        # Return the created WorkoutTemplate object
        return workout_template

    # def update(self, instance, validated_data):
    #     # Handle updating the instance with the given data
    #     # ...
    #     return instance

class UserReadSerializer(serializers.ModelSerializer):
    workout_sessions = WorkoutSessionSerializer(many=True, read_only=True)
    user_progress = UserProgressSerializer(many=True, read_only=True)
    workout_templates = WorkoutTemplateReadSerializer(many=True, read_only=True)

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
    







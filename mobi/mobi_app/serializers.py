# serializers.py

from rest_framework import serializers
from .models import Exercise, WorkoutTemplate, TemplateExercise, WorkoutSession, SessionExercise, Set, UserProgress
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class SetReadSerializer(serializers.ModelSerializer):
    """Serializer for the Set model - Read Only"""
    class Meta:
        model = Set
        fields = ['id', 'reps', 'weight', 'duration', 'notes']


class SetWriteSerializer(serializers.ModelSerializer):
    """Serializer for the Set model - Write Only"""
    class Meta:
        model = Set
        fields = ['reps', 'weight', 'duration', 'notes']

    def create(self, validated_data):
        # Retrieve session_exercise_id from the context
        session_exercise_id = self.context['session_exercise_id']
        session_exercise = SessionExercise.objects.get(id=session_exercise_id)

        # Create a new Set object using the validated_data
        set = Set.objects.create(session_exercise=session_exercise, **validated_data)
        return set
    
    def update(self, instance, validated_data):
        # Get the data from the validated_data, if not present, use the existing value
        instance.reps = validated_data.get('reps', instance.reps)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
    

class UserProgressSerializer(serializers.ModelSerializer):
    """Serializer for the UserProgress model"""
    class Meta:
        model = UserProgress
        fields = '__all__'

     
class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for the Exercise model"""
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'type']

    # validate_<field_name> is a method that is called when the serializer is validated
    # In this case name is the field name and this method is called and our function is defined
    # To capitalize each word in the name

    def validate_name(self, value):
        # Capitalize each word in the name
        value = value.title()
        return value


class SessionExerciseReadSerializer(serializers.ModelSerializer):
    """Serializer for the SessionExercise model - Read Only"""
    exercise = ExerciseSerializer(read_only=True)
    sets = SetReadSerializer(many=True, read_only=True)

    class Meta:
        model = SessionExercise
        fields = ['id', 'exercise', 'sets']

class SessionExerciseWriteSerializer(serializers.ModelSerializer):
    """Serializer for the SessionExercise model - Write Only"""
    exercise_id = serializers.IntegerField()

    class Meta:
        model = SessionExercise
        fields = ['exercise_id']

    def create(self, validated_data):
        exercise_id = validated_data.pop('exercise_id')
        exercise = Exercise.objects.get(id=exercise_id)

        # Retrieve workout_session_id from the context
        workout_session_id = self.context['workout_session_id']
        workout_session = WorkoutSession.objects.get(id=workout_session_id)

        session_exercise = SessionExercise.objects.create(exercise=exercise, workout_session=workout_session)
        return session_exercise

    
    def update(self, instance, validated_data):
        instance.sets.all().delete()
        exercise_id = validated_data.get('exercise_id')
        instance.exercise = Exercise.objects.get(id=exercise_id)
        instance.save()
        return instance

class WorkoutSessionReadSerializer(serializers.ModelSerializer):
    """Serializer for the WorkoutSession model - Read Only"""
    session_exercises = SessionExerciseReadSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutSession
        fields = ['id', 'user', 'workout_template', 'start_time', 'end_time', 'notes', 'session_exercises']

class WorkoutSessionWriteSerializer(serializers.ModelSerializer):
    """Serializer for the WorkoutSession model - Write Only"""
    class Meta:
        model = WorkoutSession
        fields = ['workout_template', 'notes']

    def create(self, validated_data):
        # Create a new WorkoutSession object using the validated_data
        workout_session = WorkoutSession.objects.create(**validated_data)

        # Copy exercises from template to session
        template_exercises = TemplateExercise.objects.filter(workout_template=validated_data['workout_template'])
        for template_exercise in template_exercises:
            SessionExercise.objects.create(
                workout_session=workout_session,
                exercise=template_exercise.exercise
            )
        return workout_session 

class TemplateExerciseSerializer(serializers.ModelSerializer):
    """Serializer for the TemplateExercise model"""
    # Include related exercise details
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = TemplateExercise
        fields = ['id', 'workout_template', 'exercise']

class WorkoutTemplateReadSerializer(serializers.ModelSerializer):
    """Serializer for the WorkoutTemplate model - Read Only"""
    template_exercises = TemplateExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutTemplate
        fields = ['id', 'user', 'name', 'description', 'created_at', 'template_exercises']


class WorkoutTemplateWriteSerializer(serializers.ModelSerializer):
    """Serializer for the WorkoutTemplate model - Write Only"""
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
    """Serializer for the User model - Read Only"""
    workout_sessions = WorkoutSessionReadSerializer(many=True, read_only=True)
    user_progress = UserProgressSerializer(many=True, read_only=True)
    workout_templates = WorkoutTemplateReadSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'workout_sessions', 'user_progress', 'workout_templates']

class UserWriteSerializer(serializers.ModelSerializer):
    """Serializer for the User model - Write Only"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        return User.objects.create(**validated_data)
    







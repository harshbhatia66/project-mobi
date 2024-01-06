from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise, WorkoutTemplate, WorkoutSession, SessionExercise, Set, UserProgress
from .serializers import UserReadSerializer, UserWriteSerializer, ExerciseSerializer, WorkoutTemplateReadSerializer, WorkoutTemplateWriteSerializer, WorkoutSessionReadSerializer, WorkoutSessionWriteSerializer, SessionExerciseSerializer, SetSerializer, UserProgressSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# import not found
from rest_framework.exceptions import NotFound
# Create your views here.
class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        # Get all users
        users = User.objects.all()
        # Serialize the users
        serializer = UserReadSerializer(users, many=True)
        # Return the serialized data
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserWriteSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            read_serializer = UserReadSerializer(user)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    """
    Retrieve, update, or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserReadSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserWriteSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(UserReadSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExerciseList(APIView):
    def get(self, request, format=None):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetail(APIView):
    def get_object(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise = self.get_object(pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkoutTemplateList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        # Filter templates by the requesting user
        workout_templates = WorkoutTemplate.objects.filter(user=request.user)
        serializer = WorkoutTemplateReadSerializer(workout_templates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a new instance of WorkoutTemplateWriteSerializer with the data from the request
        serializer = WorkoutTemplateWriteSerializer(data=request.data)

        # Check if the data in the serializer is valid
        if serializer.is_valid():
            # If the data is valid, save the serializer and create a new WorkoutTemplate object
            # The user is set to the user making the request
            workout_template = serializer.save(user=request.user)

            # Create a new instance of WorkoutTemplateReadSerializer with the created WorkoutTemplate object
            read_serializer = WorkoutTemplateReadSerializer(workout_template)

            # Return a response with the serialized WorkoutTemplate data and a 201 CREATED status
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)

        # If the data in the serializer is not valid, return a response with the serializer's errors and a 400 BAD REQUEST status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutTemplateDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, request):
        try:
            # Ensure the template belongs to the requesting user
            return WorkoutTemplate.objects.get(pk=pk, user=request.user)
        except WorkoutTemplate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        serializer = WorkoutTemplateReadSerializer(workout_template)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        serializer = WorkoutTemplateReadSerializer(workout_template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        workout_template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class WorkoutSessionList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        workout_sessions = WorkoutSession.objects.filter(user=request.user)
        serializer = WorkoutSessionReadSerializer(workout_sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutSessionWriteSerializer(data=request.data)
        if serializer.is_valid():
            workout_session = serializer.save(user=request.user)
            read_serializer = WorkoutSessionReadSerializer(workout_session)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkoutSessionDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, request):
        try:
            return WorkoutSession.objects.get(pk=pk, user=request.user)
        except WorkoutSession.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        serializer = WorkoutSessionReadSerializer(workout_session)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        serializer = WorkoutSessionWriteSerializer(workout_session, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        workout_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionExerciseList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        session_exercises = SessionExercise.objects.all()
        serializer = SessionExerciseSerializer(session_exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        workout_session_id = request.data.get('workout_session')

        # Validate workout_session_id
        if not workout_session_id:
            return Response({"error": "Workout session ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            workout_session = WorkoutSession.objects.get(id=workout_session_id)
        except WorkoutSession.DoesNotExist:
            raise NotFound("Workout session not found.")

        serializer = SessionExerciseSerializer(data=request.data, context={'workout_session': workout_session})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SessionExerciseDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, request):
        try:
            return SessionExercise.objects.get(pk=pk)
        except SessionExercise.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        session_exercise = self.get_object(pk)
        serializer = SessionExerciseSerializer(session_exercise)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        session_exercise = self.get_object(pk)
        serializer = SessionExerciseSerializer(session_exercise, data=request.data)
        if serializer.is_valid():
            serializer.save(session=request.session)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        session_exercise = self.get_object(pk)
        session_exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SetList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        sets = Set.objects.all()
        serializer = SetSerializer(sets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        session_exercise_id = request.data.get('session_exercise')
        session_exercise = SessionExercise.objects.get(id=session_exercise_id)
        serializer = SetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(session_exercise=session_exercise)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, request):
        try:
            return Set.objects.get(pk=pk)
        except Set.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        set = self.get_object(pk)
        serializer = SetSerializer(set)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        set = self.get_object(pk)
        serializer = SetSerializer(set, data=request.data)
        if serializer.is_valid():
            serializer.save(session_exercise=request.session_exercise)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        set = self.get_object(pk)
        set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserProgressDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        try:
            # Retrieve the user's progress record
            return UserProgress.objects.get(user=request.user)
        except UserProgress.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user_progress = self.get_object(request)
        serializer = UserProgressSerializer(user_progress)
        return Response(serializer.data)

    def put(self, request, format=None):
        user_progress = self.get_object(request)
        serializer = UserProgressSerializer(user_progress, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user_progress = self.get_object(request)
        user_progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

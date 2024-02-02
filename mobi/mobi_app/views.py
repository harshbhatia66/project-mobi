from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise, WorkoutTemplate, WorkoutSession, SessionExercise, Set, UserProgress
from .serializers import UserReadSerializer, UserWriteSerializer, ExerciseSerializer, WorkoutTemplateReadSerializer, WorkoutTemplateWriteSerializer, SessionExerciseWriteSerializer, WorkoutSessionReadSerializer, WorkoutSessionWriteSerializer, SessionExerciseReadSerializer, SetReadSerializer, SetWriteSerializer, UserProgressSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .utils import verify_firebase_token
import firebase_admin
from firebase_admin import auth
from rest_framework.exceptions import NotFound, PermissionDenied
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class TestToken(APIView):
    def post(self, request, format=None):
        token = request.data.get('token')

        try:
            django_token = verify_firebase_token(token)
            # If token is valid, return a success message with user details
            print('Successfully verified token.')
            print('Django Token', django_token)
            return Response({
                'message': 'Token is valid.',
                'token': django_token,
            }, status=status.HTTP_200_OK)

        except ValidationError as e:
            # Handle the validation error
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    permission_classes = [IsAuthenticated]
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
            serializer.save()
            return Response({"message": "User successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    """
    Retrieve, update, or delete a user instance.
    """
    permission_classes = [IsAuthenticated]
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
            # Return message in response and 201 CREATED status
            return Response({"message": "User successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response({"message": "User successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

class ExerciseList(APIView):
    """
    List all exercises, or create a new exercise.
    """
    def get(self, request, format=None):
        # get exercises related to the requesting user and public exercises
        exercises = Exercise.objects.filter(Q(user=request.user) | Q(user__isnull=True)).order_by('name')
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Exercise successfully created."}, status=status.HTTP_201_CREATED)
        else:
            # Customize the error response
            errors = {"errors": serializer.errors, "message": "There was a problem creating the exercise."}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetail(APIView):
    def get_object(self, pk, request):
        try:
            exercise = Exercise.objects.get(pk=pk)
            if exercise.user is None or exercise.user == request.user:
                return exercise
            raise PermissionDenied("You do not have permission to access this exercise.")
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise = self.get_object(pk, request)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise = self.get_object(pk, request)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            if exercise.user is not None and exercise.user != request.user:
                raise PermissionDenied("You cannot modify someone else's exercise.")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise = self.get_object(pk, request)
        if exercise.user is not None and exercise.user != request.user:
            raise PermissionDenied("You cannot delete someone else's exercise.")
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkoutTemplateList(APIView):
    """
    List all workout templates, or create a new workout template.
    """
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
            serializer.save(user=request.user)

            return Response({"message": "Workout template successfully created."}, status=status.HTTP_201_CREATED)

        # If the data in the serializer is not valid, return a response with the serializer's errors and a 400 BAD REQUEST status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutTemplateDetail(APIView):
    """
    Retrieve, update, or delete a workout template instance.
    """
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
            return Response({"message": "Workout template successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        workout_template.delete()
        return Response({"message": "Workout template successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

    
class WorkoutSessionList(APIView):
    """
    List all workout sessions, or create a new workout session.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        workout_sessions = WorkoutSession.objects.filter(user=request.user)
        serializer = WorkoutSessionReadSerializer(workout_sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutSessionWriteSerializer(data=request.data)
        if serializer.is_valid():
            workout_session = serializer.save(user=request.user)
            return Response({"message": "Workout session successfully created.", "id": workout_session.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkoutSessionDetail(APIView):
    """
    Retrieve, update, or delete a workout session instance.
    """
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
            return Response({"message": "Workout session successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        workout_session.delete()
        return Response({"message": "Workout session successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

class SessionExerciseList(APIView):
    """
    List all session exercises, or create a new session exercise.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, workout_session_id, format=None):
        try:
            workout_session = WorkoutSession.objects.get(pk=workout_session_id, user=request.user)
        except WorkoutSession.DoesNotExist:
            raise NotFound("Workout session not found.")

        session_exercises = SessionExercise.objects.filter(workout_session=workout_session)
        serializer = SessionExerciseReadSerializer(session_exercises, many=True)
        return Response(serializer.data)

    def post(self, request, workout_session_id, format=None):
        # Pass workout_session_id in the serializer context
        serializer_context = {
            'workout_session_id': workout_session_id,
        }
        serializer = SessionExerciseWriteSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Session exercise successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionExerciseDetail(APIView):
    """
    Retrieve, update, or delete a session exercise instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, session_exercise_id):
        try:
            return SessionExercise.objects.get(pk=session_exercise_id)
        except SessionExercise.DoesNotExist:
            raise Http404
    
    def get(self, request, session_exercise_id, format=None):
        session_exercise = self.get_object(session_exercise_id)
        serializer = SessionExerciseReadSerializer(session_exercise)
        return Response(serializer.data)
    
    def put(self, request, session_exercise_id, format=None):
        session_exercise = self.get_object(session_exercise_id)
        serializer = SessionExerciseWriteSerializer(session_exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Session exercise successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, session_exercise_id, format=None):
        session_exercise = self.get_object(session_exercise_id)
        session_exercise.delete()
        return Response({"message": "Session exercise successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    
class SetList(APIView):
    """
    List all sets, or create a new set.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        sets = Set.objects.all()
        serializer = SetReadSerializer(sets, many=True)
        return Response(serializer.data)

    def post(self, request, session_exercise_id, format=None):
        serializer_context = {
            'session_exercise_id': session_exercise_id,
        }
        serializer = SetWriteSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Set successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDetail(APIView):
    """
    Retrieve, update, or delete a set instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, set_id, request):
        try:
            return Set.objects.get(pk=set_id)
        except Set.DoesNotExist:
            raise Http404
    
    def get(self, request, set_id, format=None):
        set = self.get_object(set_id, request)
        serializer = SetReadSerializer(set)
        return Response(serializer.data)
    
    def put(self, request, set_id, format=None):
        set = self.get_object(set_id, request)
        serializer = SetWriteSerializer(set, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Set successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, set_id, format=None):
        set = self.get_object(set_id, request)
        serializer = SetWriteSerializer(set, data=request.data, partial=True)  # Note the partial=True
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Set successfully updated."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, set_id, format=None):
        set = self.get_object(set_id, request)
        set.delete()
        return Response({"message": "Set successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
    
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

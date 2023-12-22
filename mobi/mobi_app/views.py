from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Exercise, WorkoutTemplate, TemplateExercise, WorkoutSession, SessionExercise, Set, UserProgress
from .serializers import UserReadSerializer, UserWriteSerializer, ExerciseSerializer, WorkoutTemplateSerializer, TemplateExerciseSerializer, WorkoutSessionSerializer, SessionExerciseSerializer, SetSerializer, UserProgressSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

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

    def delete(self, request, pk, format=None):
        exercise = self.get_object(pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkoutTemplateList(APIView):

    def get(self, request, format=None):
        # Filter templates by the requesting user
        workout_templates = WorkoutTemplate.objects.filter(user=request.user)
        serializer = WorkoutTemplateSerializer(workout_templates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutTemplateSerializer(data=request.data)
        if serializer.is_valid():
            # Set the user to the logged-in user
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutTemplateDetail(APIView):

    def get_object(self, pk, request):
        try:
            # Ensure the template belongs to the requesting user
            return WorkoutTemplate.objects.get(pk=pk, user=request.user)
        except WorkoutTemplate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        serializer = WorkoutTemplateSerializer(workout_template)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        serializer = WorkoutTemplateSerializer(workout_template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout_template = self.get_object(pk, request)
        workout_template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class TemplateExerciseList(APIView):
    def get(self, request, format=None):
        template_exercises = TemplateExercise.objects.filter(user=request.user)
        serializer = TemplateExerciseSerializer(template_exercises, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TemplateExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TemplateExerciseDetail(APIView):
    def get_object(self, pk, request):
        try:
            template_exercise = TemplateExercise.objects.get(pk=pk)
            if template_exercise.workout_template.user != request.user:
                raise Http404  # or return a permission denied response
            return template_exercise
        except TemplateExercise.DoesNotExist:
            raise Http404

    
    def get(self, request, pk, format=None):
        template_exercise = self.get_object(pk)
        serializer = TemplateExerciseSerializer(template_exercise)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        template_exercise = self.get_object(pk)
        serializer = TemplateExerciseSerializer(template_exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        template_exercise = self.get_object(pk)
        template_exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WorkoutSessionList(APIView):
    def get(self, request, format=None):
        workout_sessions = WorkoutSession.objects.all()
        serializer = WorkoutSessionSerializer(workout_sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkoutSessionDetail(APIView):
    def get_object(self, pk, request):
        try:
            return WorkoutSession.objects.get(pk=pk, user=request.user)
        except WorkoutSession.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        serializer = WorkoutSessionSerializer(workout_session)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        serializer = WorkoutSessionSerializer(workout_session, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        workout_session = self.get_object(pk, request)
        workout_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SessionExerciseList(APIView):
    def get(self, request, format=None):
        session_exercises = SessionExercise.objects.all()
        serializer = SessionExerciseSerializer(session_exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        workout_session_id = request.data.get('workout_session')
        workout_session = WorkoutSession.objects.get(id=workout_session_id)
        serializer = SessionExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(workout_session=workout_session)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionExerciseDetail(APIView):
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

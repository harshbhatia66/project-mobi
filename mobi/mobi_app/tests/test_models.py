from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from mobi_app.models import Exercise, WorkoutTemplate, TemplateExercise, WorkoutSession, SessionExercise, Set, UserProgress
# import validation error
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseTest(TestCase):
    def setUp(self):
        # User setup
        self.user_01 = User.objects.create_user(username='testuser', password='12345')

        self.user_02 = User.objects.create_user(username='testuser2', password='12345')

        # Exercise setup 
        self.global_exercise_name_01 = "Bench Press"
        self.global_exercise_description_01 = "A chest exercise involving pushing weight upwards from a bench."
        self.global_exercise_type_01 = "Chest"

        self.global_exercise_name_02 = "Incline Bench Press"
        self.global_exercise_description_02 = "An upper chest exercise performed on an inclined bench."
        self.global_exercise_type_02 = "Chest"

        self.global_exercise_name_03 = "Low to High Rows"
        self.global_exercise_description_03 = "A back exercise involving pulling weight from a low to high position."
        self.global_exercise_type_03 = "Back"

        self.global_exercise_name_04 = "Dips"
        self.global_exercise_description_04 = "A compound exercise for the chest and triceps, usually performed on parallel bars."
        self.global_exercise_type_04 = "Chest"

        self.global_exercise_name_05 = "Pull Ups"
        self.global_exercise_description_05 = "An upper body exercise involving pulling the body weight upward using a horizontal bar."
        self.global_exercise_type_05 = "Back"

        self.global_exercise_name_06 = "Seated Row Close Grip"
        self.global_exercise_description_06 = "A back exercise using a close grip handle on a seated row machine."
        self.global_exercise_type_06 = "Back"

        self.global_exercise_name_07 = "Incline Chest Flies"
        self.global_exercise_description_07 = "A chest isolation exercise performed on an inclined bench, focusing on chest muscles."
        self.global_exercise_type_07 = "Chest"

        # Exercise 08
        self.global_exercise_name_08 = "Hammer Strength Shoulder Press"
        self.global_exercise_description_08 = "A shoulder exercise using the Hammer Strength machine, targeting the deltoid muscles."
        self.global_exercise_type_08 = "Shoulders"

        # Exercise 09
        self.global_exercise_name_09 = "Incline Dumbbell Curls"
        self.global_exercise_description_09 = "A bicep exercise performed on an inclined bench using dumbbells, emphasizing the bicep muscles."
        self.global_exercise_type_09 = "Arms"

        # Exercise 10
        self.global_exercise_name_10 = "Tricep Pushdowns"
        self.global_exercise_description_10 = "A tricep isolation exercise using a cable machine and rope attachment to work the triceps."
        self.global_exercise_type_10 = "Arms"

        # Exercise 11
        self.global_exercise_name_11 = "Dumbbell Lateral Raises"
        self.global_exercise_description_11 = "A shoulder exercise involving raising dumbbells to the side to target the lateral deltoid muscles."
        self.global_exercise_type_11 = "Shoulders"

        # Exercise 12
        self.global_exercise_name_12 = "Preacher Curls"
        self.global_exercise_description_12 = "A bicep exercise using a preacher bench to isolate and strengthen the biceps."
        self.global_exercise_type_12 = "Arms"

        # Exercise 13
        self.global_exercise_name_13 = "Tricep Rope Extension"
        self.global_exercise_description_13 = "A tricep exercise using a rope attachment on a cable machine to effectively target the triceps."
        self.global_exercise_type_13 = "Arms"

        # Exercise 14
        self.global_exercise_name_14 = "Calf Raises"
        self.global_exercise_description_14 = "A calf exercise that involves raising your heels to target the calf muscles."
        self.global_exercise_type_14 = "Legs"

        # Exercise 15
        self.global_exercise_name_15 = "Leg Extensions"
        self.global_exercise_description_15 = "A quadriceps isolation exercise using a leg extension machine to strengthen the front thigh muscles."
        self.global_exercise_type_15 = "Legs"

        # Exercise 16
        self.global_exercise_name_16 = "Hamstring Curls"
        self.global_exercise_description_16 = "A hamstring exercise performed on a machine to target the back of the thigh muscles."
        self.global_exercise_type_16 = "Legs"

        # Exercise 17
        self.global_exercise_name_17 = "Hack Squat"
        self.global_exercise_description_17 = "A compound leg exercise using a hack squat machine to work the quadriceps and glutes."
        self.global_exercise_type_17 = "Legs"

        # Exercise 18
        self.global_exercise_name_18 = "Squat Press"
        self.global_exercise_description_18 = "A leg press variation that involves squatting with a press to target the quadriceps, hamstrings, and glutes."
        self.global_exercise_type_18 = "Legs"

        # Exercise 19
        self.global_exercise_name_19 = "Leg Raises"
        self.global_exercise_description_19 = "A core exercise involving raising your legs from a hanging position to strengthen the lower abdominal muscles."
        self.global_exercise_type_19 = "Core"

        # Exercise 20
        self.global_exercise_name_20 = "Machine Crunch"
        self.global_exercise_description_20 = "A core exercise using a machine to perform crunches, targeting the abdominal muscles."
        self.global_exercise_type_20 = "Core"


        for i in range(1, 21):
            i_formatted = f'{i:02}'  # Formats the index to be two digits
            setattr(self, f'global_exercise_{i_formatted}', Exercise.objects.create(
                name=getattr(self, f'global_exercise_name_{i_formatted}'),
                description=getattr(self, f'global_exercise_description_{i_formatted}'),
                type=getattr(self, f'global_exercise_type_{i_formatted}')
            ))

        # Create a user specific exercise
        self.user_exercise_01 = Exercise.objects.create(
            user=self.user_01,
            name="Close Grip Bench Press",
            description="A chest exercise involving pushing weight upwards from a bench with a narrow grip.",
            type="Chest"
        )

        # Exercise 2
        self.user_exercise_02 = Exercise.objects.create(
            user=self.user_01,
            name="Turkish Get-Up",
            description="A full-body exercise that involves getting up from a lying position while holding a kettlebell or dumbbell overhead.",
            type="Full Body"
        )

        # Exercise 3
        self.user_exercise_03 = Exercise.objects.create(
            user=self.user_01,
            name="Dragon Flags",
            description="A challenging core exercise that requires lying on a bench and lifting your legs and lower back off the bench while keeping your upper body stationary.",
            type="Core"
        )

        # Exercise 4
        self.user_exercise_04 = Exercise.objects.create(
            user=self.user_01,
            name="Single-Leg Romanian Deadlift",
            description="A unilateral exercise that targets the hamstrings and lower back by balancing on one leg and lowering a dumbbell or kettlebell toward the ground.",
            type="Legs"
        )

        # Exercise 5
        self.user_exercise_05 = Exercise.objects.create(
            user=self.user_01,
            name="Zercher Squats",
            description="A squat variation where the barbell is held in the crook of the elbows, challenging the core and upper back while working the legs.",
            type="Legs"
        )

        self.workout_template_name_01 = "Chest and Back"
        self.workout_template_description_01 = "A chest and back workout"

        self.workout_template_name_02 = "Arms and Shoulders"
        self.workout_template_description_02 = "An arms and shoulders workout"

        self.workout_template_name_03 = "Legs and Core"
        self.workout_template_description_03 = "A legs and core workout"

        self.workout_template_name_04 = "Chest and Back Alt"
        self.workout_template_description_04 = "A chest and back workout"

        self.workout_template_name_05 = "Arms and Shoulders Alt"
        self.workout_template_description_05 = "An arms and shoulders workout"

        self.workout_template_name_06 = "Legs and Core Alt"
        self.workout_template_description_06 = "A legs and core workout"

        # Create the workout templates
        self.workout_template_01 = WorkoutTemplate.objects.create(
            user=self.user_01,
            name=self.workout_template_name_01,
            description=self.workout_template_description_01,
        )

        self.workout_template_02 = WorkoutTemplate.objects.create(
            user=self.user_01,
            name=self.workout_template_name_02,
            description=self.workout_template_description_02,
        )

        self.workout_template_03 = WorkoutTemplate.objects.create(
            user=self.user_01,
            name=self.workout_template_name_03,
            description=self.workout_template_description_03,
        )

        # List of global exercises
        workout_template_01_exercises = [
            self.global_exercise_01,
            self.global_exercise_02,
            self.global_exercise_03,
            self.global_exercise_04,
            self.global_exercise_05,
            self.global_exercise_06,
            self.global_exercise_07
        ]

        # Add exercises to workout template 01
        for exercise in workout_template_01_exercises:
            TemplateExercise.objects.create(
                workout_template=self.workout_template_01,
                exercise=exercise
            )

class ExerciseModelTest(BaseTest):

    def setUp(self):
        super().setUp()

    # Test model instance creation
    def test_model_creation_in_db(self):
        self.assertEqual(Exercise.objects.count(), 25)

    # Test global exercise creation
    def test_global_exercise_creation(self):
        self.assertIsNone(self.global_exercise_01.user, "Global exercise should not have a user associated")
        self.assertEqual(self.global_exercise_01.name, self.global_exercise_name_01)
        self.assertEqual(self.global_exercise_01.description, self.global_exercise_description_01)
        self.assertEqual(self.global_exercise_01.type, self.global_exercise_type_01)

    # Test field validations
    def test_name_max_length(self):
        max_length = self.global_exercise_01._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    # Test if a name longer than 255 characters is invalid and raises an error
    def test_name_max_length_validation(self):
        exercise_name = "x" * 256
        with self.assertRaises(Exception):
            Exercise.objects.create(
                name=exercise_name, 
                description=self.global_exercise_description_01, 
                type=self.global_exercise_type_01
            )

    # Test if all fields are required
    def test_fields_required(self):
        with self.assertRaises(ValidationError):
            exercise = Exercise(
                description=self.global_exercise_description_01, 
                type=self.global_exercise_type_01
            )
            exercise.full_clean()

        with self.assertRaises(ValidationError):
            exercise = Exercise(
                name=self.global_exercise_name_01, 
                type=self.global_exercise_type_01
            )
            exercise.full_clean()

        with self.assertRaises(ValidationError):
            exercise = Exercise(
                name=self.global_exercise_name_01, 
                description=self.global_exercise_description_01
            )
            exercise.full_clean()

    # Test string representation
    def test_string_representation(self):
        self.assertEqual(str(self.global_exercise_name_01), self.global_exercise_name_01)

    # Test model field types
    def test_name_field_type(self):
        self.assertEqual(self.global_exercise_01._meta.get_field('name').get_internal_type(), 'CharField')
        self.assertEqual(self.global_exercise_01._meta.get_field('description').get_internal_type(), 'TextField')
        self.assertEqual(self.global_exercise_01._meta.get_field('type').get_internal_type(), 'CharField')

    # Test user specific exercise creation
    def test_user_exercise_creation(self):
        self.assertEqual(self.user_exercise_01.user, self.user_01)
        self.assertEqual(self.user_exercise_01.name, "Close Grip Bench Press")
        self.assertEqual(self.user_exercise_01.description, "A chest exercise involving pushing weight upwards from a bench with a narrow grip.")
        self.assertEqual(self.user_exercise_01.type, "Chest")

    # Test user association integrity
    # Ensure that a user can only see their own exercises and not other users
    def test_user_association_integrity(self):
        self.assertEqual(self.user_exercise_01.user, self.user_01)
        self.assertNotEqual(self.user_exercise_01.user, self.user_02)

        # Assert that user 02 does not have any user specific exercises
        self.assertEqual(self.user_02.exercises.count(), 0)
        
    # Test exercise visibility and isolation
    # Ensure that a user can only see their own exercises and not other users
    def test_exercise_visibility(self):
        # Assert that user 02 does not have any user specific exercises
        self.assertEqual(self.user_02.exercises.count(), 0)

        # Assert that user 02 cannot see user 01's exercise
        self.assertEqual(self.user_02.exercises.filter(name="Close Grip Bench Press").count(), 0)

        # Assert that user 01 can see their own exercise
        self.assertEqual(self.user_01.exercises.filter(name="Close Grip Bench Press").count(), 1)
        
    # Test exercise deletion with user association
    def test_user_association_deletion(self):
        self.assertEqual(self.user_exercise_01.user, self.user_01)
        # store the number of exercises associated with user 01
        user_specific_exercises = self.user_01.exercises.count()

        # Count the number of Exercise objects before the deletion
        exercise_count_before = Exercise.objects.count()

        # Delete the user
        self.user_01.delete()

        # Count the number of Exercise objects after the deletion
        exercise_count_after = Exercise.objects.count()

        # Assert that the number of Exercise objects has decreased by 1
        self.assertEqual(exercise_count_before - exercise_count_after, user_specific_exercises)

    # Test for when a user creates a new user specific exercise with the same name as a global exercise, this should not be allowed and should raise an error
    def test_user_exercise_name_uniqueness(self):
        with self.assertRaises(Exception):
            Exercise.objects.create(
                user=self.user_01,
                name=self.global_exercise_01,
                description=self.global_exercise_description_01,
                type=self.global_exercise_type_01
            )

class WorkoutTemplateTest(BaseTest):
    def setUp(self):
        super().setUp()


    def test_workout_template_creation(self):
        """
        Test the creation of a WorkoutTemplate instance and its properties.
        """
        self.assertEqual(self.workout_template_01.user, self.user_01)
        self.assertEqual(self.workout_template_01.name, self.workout_template_name_01)
        self.assertEqual(self.workout_template_01.description, self.workout_template_description_01)

    def test_user_association(self):
        """
        Test that a WorkoutTemplate is correctly associated with a User.
        """
        self.assertEqual(self.workout_template_01.user, self.user_01)

        # Test the workout tempalte does not belong to user 02
        self.assertNotEqual(self.workout_template_01.user, self.user_02)


    def test_workout_template_string_representation(self):
        """
        Test the string representation of the WorkoutTemplate instance.
        """
        self.assertEqual(str(self.workout_template_01.name), self.workout_template_name_01)

    def test_template_name_max_length(self):
        """
        Test that the 'name' field does not exceed the maximum length.
        """
        max_length = self.workout_template_01._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_cascade_delete_user(self):
        """
        Test that deleting a User also deletes the associated WorkoutTemplate(s).
        """
        # Count the number of WorkoutTemplate objects before the deletion
        workout_template_count_before = WorkoutTemplate.objects.count()

        # Count the users workout templates
        user_workout_template_count = self.user_01.workout_templates.count()

        # Delete the user
        self.user_01.delete()

        # Count the number of WorkoutTemplate objects after the deletion
        workout_template_count_after = WorkoutTemplate.objects.count()

        # Assert that the number of WorkoutTemplate objects has decreased
        self.assertEqual(workout_template_count_before - workout_template_count_after, user_workout_template_count)

    def test_template_creation_with_missing_user(self):
        """
        Test the behavior when creating a WorkoutTemplate without a user.
        """
        with self.assertRaises(Exception):
            WorkoutTemplate.objects.create(
                name=self.workout_template_name_01,
                description=self.workout_template_description_01,
            ).full_clean()
      
    def test_template_creation_with_missing_name(self):
        """
        Test the behavior when creating a WorkoutTemplate without a name.
        """
        with self.assertRaises(Exception):
            WorkoutTemplate.objects.create(
                user=self.user_01,
                description=self.workout_template_description_01,
            ).full_clean()

    def test_creation_date_auto_set(self):
        """
        Test that the creation date is automatically set upon creating a WorkoutTemplate.
        """
        self.assertIsNotNone(self.workout_template_01.created_at)


    def test_duplicate_workout_template_for_user(self):
        """
        Test the behavior when attempting to create a duplicate WorkoutTemplate for the same user.
        """
        with self.assertRaises(Exception):
            WorkoutTemplate.objects.create(
                user=self.user_01,
                name=self.workout_template_name_01,
                description=self.workout_template_description_01,
            ).full_clean()

    def test_workout_template_with_invalid_user(self):
        """
        Test creating a WorkoutTemplate with an invalid or non-existent user.
        """
        with self.assertRaises(Exception):
            WorkoutTemplate.objects.create(
                user=3,
                name=self.workout_template_name_01,
                description=self.workout_template_description_01,
            ).full_clean()

    def test_template_description_optional(self):
        """
        Test that the description field is optional for a WorkoutTemplate.
        """
        WorkoutTemplate.objects.create(
            user=self.user_01,
            name=self.workout_template_name_04,
        ).full_clean()

    def test_user_workout_template_isolation(self):
        """
        Test that users can only access their own workout templates and not those of other users.
        """
        # Assert that user 02 does not have any workout templates
        self.assertEqual(self.user_02.workout_templates.count(), 0)

        # Assert that user 02 cannot see user 01's workout template
        self.assertEqual(self.user_02.workout_templates.filter(name=self.workout_template_name_01).count(), 0)

        # Assert that user 01 can see their own workout template
        self.assertEqual(self.user_01.workout_templates.filter(name=self.workout_template_name_01).count(), 1)

    def test_user_specific_workout_template_count(self):
        """
        Test that the correct number of workout templates are associated with each user.
        """
        self.assertEqual(self.user_01.workout_templates.count(), 3)
        self.assertEqual(self.user_02.workout_templates.count(), 0)


    def test_create_duplicate_workout_template_for_different_users(self):
        """
        Test the behavior of creating workout templates with the same name for different users.
        """
        # Count the number of WorkoutTemplate objects before the creation
        workout_template_count_before = WorkoutTemplate.objects.count()

        # Create a workout template with the same name for user 02
        WorkoutTemplate.objects.create(
            user=self.user_02,
            name=self.workout_template_name_01,
            description=self.workout_template_description_01,
        ).full_clean()

        # Count the number of WorkoutTemplate objects after the creation
        workout_template_count_after = WorkoutTemplate.objects.count()

        # Assert that the number of WorkoutTemplate objects has increased by 1
        self.assertEqual(workout_template_count_after - workout_template_count_before, 1)
    
    def test_adding_template_exercise_to_workout_template(self):
        """
        Test adding a TemplateExercise to a WorkoutTemplate.
        """
        # Count the number of TemplateExercise objects before the creation
        template_exercise_count_before = TemplateExercise.objects.count()

        # Create a new TemplateExercise
        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_08
        )

        # Count the number of TemplateExercise objects after the creation
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has increased by 1
        self.assertEqual(template_exercise_count_after - template_exercise_count_before, 1)

    def test_workout_template_exercise_count(self):
        """
        Test the count of TemplateExercises in a WorkoutTemplate.
        """
        self.assertEqual(self.workout_template_01.template_exercises.count(), 7)

    def test_remove_template_exercise_from_workout_template(self):
        """
        Test removing a TemplateExercise from a WorkoutTemplate.
        """
        # Count the number of TemplateExercise objects before the deletion
        template_exercise_count_before = TemplateExercise.objects.count()

        # Delete a TemplateExercise
        self.workout_template_01.template_exercises.filter(exercise=self.global_exercise_01).delete()

        # Count the number of TemplateExercise objects after the deletion
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has decreased by 1
        self.assertEqual(template_exercise_count_before - template_exercise_count_after, 1)

    def test_cascade_delete_workout_template_with_template_exercises(self):
        """
        Test that deleting a WorkoutTemplate also deletes associated TemplateExercises.
        """
        # Count the number of TemplateExercise objects before the deletion
        template_exercise_count_before = TemplateExercise.objects.count()
        
        # Count the number of template exercises associated with the workout template
        template_exercise_count_in_workout_template = self.workout_template_01.template_exercises.count()

        # Delete the WorkoutTemplate
        self.workout_template_01.delete()

        # Count the number of TemplateExercise objects after the deletion
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has decreased
        self.assertEqual(template_exercise_count_before - template_exercise_count_after, template_exercise_count_in_workout_template)

    #Test that deleting a global exercise also deletes associated TemplateExercises and reduces workout template exercise count.
    def test_cascade_delete_global_exercise_with_template_exercises(self):
        """
        Test that deleting a global exercise also deletes associated TemplateExercises and reduces workout template exercise count.
        """
        # Count the number of TemplateExercise objects before the deletion
        template_exercise_count_before = TemplateExercise.objects.count()

        # Count the number of template exercises associated with the workout template
        template_exercise_count_in_workout_template = self.workout_template_01.template_exercises.count()

        # Delete the global exercise
        self.global_exercise_01.delete()

        # Count the number of TemplateExercise objects after the deletion
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has decreased
        self.assertEqual(template_exercise_count_before - template_exercise_count_after, 1)

        template_exercise_count_in_workout_template_after = self.workout_template_01.template_exercises.count()

        # Assert that the number of TemplateExercise objects associated with the workout template has decreased
        self.assertEqual(template_exercise_count_in_workout_template - template_exercise_count_in_workout_template_after, 1)

class TemplateExerciseTest(BaseTest):
    def setUp(self):
        super().setUp()

    def test_template_exercise_creation(self):
        """
        Test creating a TemplateExercise and verify its properties.
        """
        # Count the number of TemplateExercise objects before the creation
        template_exercise_count_before = TemplateExercise.objects.count()

        # Create a new TemplateExercise
        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_08
        )

        # Count the number of TemplateExercise objects after the creation
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has increased by 1
        self.assertEqual(template_exercise_count_after - template_exercise_count_before, 1)

    def test_template_exercise_association_with_workout_template(self):
        """
        Test the association of a TemplateExercise with a WorkoutTemplate.
        """
        # Create a new TemplateExercise
        template_exercise = TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_08
        )

        self.assertEqual(template_exercise.workout_template, self.workout_template_01)


    def test_template_exercise_association_with_exercise(self):
        """
        Test the association of a TemplateExercise with an Exercise.
        """
        # Create a new TemplateExercise
        template_exercise = TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_08
        )

        self.assertEqual(template_exercise.exercise, self.global_exercise_08)

    def test_cascade_delete_on_workout_template_deletion(self):
        """
        Test that deleting a WorkoutTemplate deletes its associated TemplateExercises.
        """
        # Count the number of TemplateExercise objects before the deletion
        template_exercise_count_before = TemplateExercise.objects.count()

        # Count the number of template exercises associated with the workout template
        template_exercise_count_in_workout_template = self.workout_template_01.template_exercises.count()

        # Delete the WorkoutTemplate
        self.workout_template_01.delete()

        # Count the number of TemplateExercise objects after the deletion
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has decreased
        self.assertEqual(template_exercise_count_before - template_exercise_count_after, template_exercise_count_in_workout_template)

    def test_cascade_delete_on_exercise_deletion(self):
        """
        Test that deleting an Exercise deletes its associated TemplateExercises.
        """
        # Count the number of TemplateExercise objects before the deletion
        template_exercise_count_before = TemplateExercise.objects.count()

        # Count the number of template exercises associated with the workout template
        template_exercise_count_in_workout_template = self.workout_template_01.template_exercises.count()

        # Delete the Exercise
        self.global_exercise_01.delete()

        # Count the number of TemplateExercise objects after the deletion
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has decreased
        self.assertEqual(template_exercise_count_before - template_exercise_count_after, 1)

        template_exercise_count_in_workout_template_after = self.workout_template_01.template_exercises.count()

        # Assert that the number of TemplateExercise objects associated with the workout template has decreased
        self.assertEqual(template_exercise_count_in_workout_template - template_exercise_count_in_workout_template_after, 1)

    def test_template_exercise_uniqueness_in_workout_template(self):
        """
        Test that the same exercise can be added multiple times to the same WorkoutTemplate.
        """
        # Count the number of TemplateExercise objects before the creation
        template_exercise_count_before = TemplateExercise.objects.count()

        # Count the number of template exercises associated with the workout template
        template_exercise_count_in_workout_template = self.workout_template_01.template_exercises.count()

        # Create a new TemplateExercise of the same exercise that already exists in the workout template
        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_01
        )

        # Count the number of TemplateExercise objects after the creation
        template_exercise_count_after = TemplateExercise.objects.count()

        # Assert that the number of TemplateExercise objects has increased by 1
        self.assertEqual(template_exercise_count_after - template_exercise_count_before, 1)

        # Assert that the number of TemplateExercise objects associated with the workout template has increased by 1
        self.assertEqual(template_exercise_count_in_workout_template + 1, self.workout_template_01.template_exercises.count())


    def test_template_exercise_ordering_within_workout_template(self):
        """
        Test if exercises within a WorkoutTemplate maintain a specific order, if applicable.
        """
        # Add three exercises to the workout template
        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_08
        )

        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_09
        )

        TemplateExercise.objects.create(
            workout_template=self.workout_template_01,
            exercise=self.global_exercise_10
        )

        # Get the exercises in the workout template and check if they are in the correct order
        exercises = self.workout_template_01.template_exercises.all()

        # Check the order
        for i in range(10):
            i_formatted = f'{i+1:02}'  # Formats the index to be two digits
            self.assertEqual(exercises[i].exercise, getattr(self, f'global_exercise_{i_formatted}'))

    def test_template_exercise_visibility_to_different_users(self):
        """
        Test that a TemplateExercise is visible only to the user associated with the WorkoutTemplate.
        """
        # Assert that user 02 does not have any workout templates
        self.assertEqual(self.user_02.workout_templates.count(), 0)

        # Assert that user 02 cannot see user 01's workout template
        self.assertEqual(self.user_02.workout_templates.filter(name=self.workout_template_name_01).count(), 0)

        # Assert that user 01 can see their own workout template
        self.assertEqual(self.user_01.workout_templates.filter(name=self.workout_template_name_01).count(), 1)

        # Create a workout template for user 02 with the same name as user 01's workout template and add an exercise
        user_02s_workout_template = WorkoutTemplate.objects.create(
            user=self.user_02,
            name=self.workout_template_name_01,
            description=self.workout_template_description_01,
        )

        TemplateExercise.objects.create(
            workout_template=user_02s_workout_template,
            exercise=self.global_exercise_01
        )

        # Assert that user 02 cannot see user 01's template exercises by checking the count
        self.assertEqual(self.user_02.workout_templates.filter(name=self.workout_template_name_01).first().template_exercises.count(), 1)

        # Assert that user 01 can see their own template exercises
        self.assertEqual(self.user_01.workout_templates.filter(name=self.workout_template_name_01).first().template_exercises.count(), 7)

    def test_updating_template_exercise(self):
        """
        Test updating properties of a TemplateExercise.
        """
        # Get the first TemplateExercise in the workout template
        template_exercise = self.workout_template_01.template_exercises.first()

        # Update the exercise
        template_exercise.exercise = self.global_exercise_08
        template_exercise.save()

        # Assert that the exercise has been updated
        self.assertEqual(template_exercise.exercise, self.global_exercise_08)

    def test_template_exercise_with_invalid_workout_template(self):
        """
        Test behavior when creating a TemplateExercise with an invalid or non-existent WorkoutTemplate.
        """
        # Assert error is raised when creating a TemplateExercise with an invalid WorkoutTemplate
        with self.assertRaises(Exception):
            TemplateExercise.objects.create(
                workout_template=3,
                exercise=self.global_exercise_08
            ).full_clean()

    def test_template_exercise_with_invalid_exercise(self):
        """
        Test behavior when creating a TemplateExercise with an invalid or non-existent Exercise.
        """
        # Assert error is raised when creating a TemplateExercise with an invalid Exercise
        with self.assertRaises(Exception):
            TemplateExercise.objects.create(
                workout_template=self.workout_template_01,
                exercise=3
            ).full_clean()

class WorkoutSessionTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Create a new WorkoutSession from the WorkoutTemplate
        self.workout_session_01 = WorkoutSession.objects.create(
            user=self.user_01,
            workout_template=self.workout_template_01
        )

    def test_workout_session_creation(self):
        """
        Test creating a WorkoutSession and verifying its properties.
        """

        # Assert that the WorkoutSession created in the setup exists
        self.assertIsNotNone(self.workout_session_01)

    def test_workout_session_association_with_user(self):
        """
        Test the association of a WorkoutSession with a User.
        """

        # Assert that the WorkoutSession has been created and associated with user 01
        self.assertEqual(self.workout_session_01.user, self.user_01)

        # Assert that the WorkoutSession does not belong to user 02
        self.assertNotEqual(self.workout_session_01.user, self.user_02)

    def test_workout_session_association_with_workout_template(self):
        """
        Test the association of a WorkoutSession with a WorkoutTemplate.
        """
            
        # Assert that the WorkoutSession has been created and associated with the workout template
        self.assertEqual(self.workout_session_01.workout_template, self.workout_template_01)

    def test_workout_session_start_time_auto_set(self):
        """
        Test that the start time is automatically set upon creating a WorkoutSession.
        """
        self.assertIsNotNone(self.workout_session_01.start_time)

    def test_workout_session_end_time(self):
        """
        Test setting and retrieving the end time of a WorkoutSession.
        """
        # Assert that the end time is initially None
        self.assertIsNone(self.workout_session_01.end_time)

        # Set the end time
        self.workout_session_01.end_time = timezone.now()
        self.workout_session_01.save()

        # Assert that the end time has been set
        self.assertIsNotNone(self.workout_session_01.end_time)

    def test_workout_session_notes_field(self):
        """
        Test the functionality of the notes field in a WorkoutSession.
        """
        # Create a workout session with notes
        workout_session = WorkoutSession.objects.create(
            user=self.user_01,
            workout_template=self.workout_template_01,
            notes="This is a test note."
        )

        # Assert that the notes field has been set
        self.assertEqual(workout_session.notes, "This is a test note.")

    def test_cascade_delete_on_user_deletion(self):
        """
        Test that deleting a User also deletes their WorkoutSessions.
        """
        # Count the number of WorkoutSession objects before the deletion
        workout_session_count_before = WorkoutSession.objects.count()

        # Count the number of workout sessions associated with the user
        workout_session_count_for_user = self.user_01.workout_sessions.count()

        # Delete the user
        self.user_01.delete()

        # Count the number of WorkoutSession objects after the deletion
        workout_session_count_after = WorkoutSession.objects.count()

        # Assert that the number of WorkoutSession objects has decreased
        self.assertEqual(workout_session_count_before - workout_session_count_after, workout_session_count_for_user)

    def test_cascade_delete_on_workout_template_deletion(self):
        """
        Test that deleting a WorkoutTemplate does not delete associated WorkoutSessions.
        """
        # Count the number of WorkoutSession objects before the deletion
        workout_session_count_before = WorkoutSession.objects.count()

        # Delete the WorkoutTemplate
        self.workout_template_01.delete()

        # Count the number of WorkoutSession objects after the deletion
        workout_session_count_after = WorkoutSession.objects.count()

        # Assert that the number of WorkoutSession objects has not decreased
        self.assertEqual(workout_session_count_before, workout_session_count_after)
        

    def test_updating_workout_session(self):
        """
        Test updating various fields of an existing WorkoutSession.
        """
        # Update the workout session
        self.workout_session_01.notes = "This is a test note."
        self.workout_session_01.end_time = timezone.now()
        self.workout_session_01.save()

        # Assert that the workout session has been updated
        self.assertEqual(self.workout_session_01.notes, "This is a test note.")
        self.assertIsNotNone(self.workout_session_01.end_time)

        # Update the fields again
        self.workout_session_01.notes = "This is another test note."
        # Set the end time as 2 hours after the start time
        end_time = self.workout_session_01.start_time + timedelta(hours=2)
        self.workout_session_01.end_time = end_time
        self.workout_session_01.save()
         
        # Assert that the notes field has been updated
        self.assertEqual(self.workout_session_01.notes, "This is another test note.")
        # Assert that the end time has been updated
        self.assertEqual(self.workout_session_01.end_time, end_time)

    def test_workout_session_with_invalid_user(self):
        """
        Test creating a WorkoutSession with an invalid or non-existent user.
        """
        with self.assertRaises(Exception):
            WorkoutSession.objects.create(
                user=3,
                workout_template=self.workout_template_01
            ).full_clean()

    def test_workout_session_with_invalid_workout_template(self):
        """
        Test creating a WorkoutSession with an invalid or non-existent WorkoutTemplate.
        """
        with self.assertRaises(Exception):
            WorkoutSession.objects.create(
                user=self.user_01,
                workout_template=3
            ).full_clean()

    def test_workout_session_visibility_to_user(self):
        """
        Test that a WorkoutSession is visible only to the user who created it.
        """
        # Assert that user 02 does not have any workout sessions
        self.assertEqual(self.user_02.workout_sessions.count(), 0)

        # Assert that user 02 cannot see user 01's workout session
        self.assertEqual(self.user_02.workout_sessions.filter(workout_template=self.workout_template_01).count(), 0)

        # Assert that user 01 can see their own workout session
        self.assertEqual(self.user_01.workout_sessions.filter(workout_template=self.workout_template_01).count(), 1)

        # Create a workout template for user 02
        user_02s_workout_template = WorkoutTemplate.objects.create(
            user=self.user_02,
            name=self.workout_template_name_01,
            description=self.workout_template_description_01,
        )

        # Create a workout session for user 02
        WorkoutSession.objects.create(
            user=self.user_02,
            workout_template=user_02s_workout_template
        )

        # Assert that user 02 cannot see user 01's workout session by checking the count
        self.assertEqual(self.user_02.workout_sessions.filter(workout_template=self.workout_template_01).count(), 0)

        # Assert that user 02 can see their own workout session
        self.assertEqual(self.user_02.workout_sessions.filter(workout_template=user_02s_workout_template).count(), 1)

        # Assert that user 01 can see their own workout session
        self.assertEqual(self.user_01.workout_sessions.filter(workout_template=self.workout_template_01).count(), 1)

    def test_concurrent_workout_sessions_for_user(self):
        """
        Test if a user is not allowed to have multiple concurrent workout sessions.
        """
        # Since there is already a workout session for user 01, try to create another one
        with self.assertRaises(Exception):
            WorkoutSession.objects.create(
                user=self.user_01,
                workout_template=self.workout_template_01
            ).full_clean()

        # End the first workout session
        self.workout_session_01.end_time = timezone.now()

        # Create another workout session for user 01
        WorkoutSession.objects.create(
            user=self.user_01,
            workout_template=self.workout_template_01
        ).full_clean()

        # Assert that user 01 now has two workout sessions
        self.assertEqual(self.user_01.workout_sessions.count(), 2)

    def test_access_control_for_editing_workout_session(self):
        """
        Test that only the user who created the workout session can edit it.
        """
        # Assert that user 02 cannot edit user 01's workout session
        with self.assertRaises(Exception):
            self.user_02.workout_sessions.filter(workout_template=self.workout_template_01).first().save()

        # Assert that user 01 can edit their own workout session
        self.user_01.workout_sessions.filter(workout_template=self.workout_template_01).first().save()


    def test_impact_of_workout_template_changes_on_active_sessions(self):
        """
        Test how changes to a WorkoutTemplate affect ongoing or future WorkoutSessions.
        """
        # Changing the workout template should not affect the workout session that has already started - it should still have the same exercises
        # TODO: in endpoints and views
        pass









    

    

    
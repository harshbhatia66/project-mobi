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


        # Create a global exercise
        self.global_exercise_01 = Exercise.objects.create(
            name=self.global_exercise_name_01, 
            description=self.global_exercise_description_01, 
            type=self.global_exercise_type_01
        )

        self.global_exercise_02 = Exercise.objects.create(
            name=self.global_exercise_name_02,
            description=self.global_exercise_description_02,
            type=self.global_exercise_type_02
        )

        self.global_exercise_03 = Exercise.objects.create(
            name=self.global_exercise_name_03,
            description=self.global_exercise_description_03,
            type=self.global_exercise_type_03
        )

        self.global_exercise_04 = Exercise.objects.create(
            name=self.global_exercise_name_04,
            description=self.global_exercise_description_04,
            type=self.global_exercise_type_04
        )

        self.global_exercise_05 = Exercise.objects.create(
            name=self.global_exercise_name_05,
            description=self.global_exercise_description_05,
            type=self.global_exercise_type_05
        )

        self.global_exercise_06 = Exercise.objects.create(
            name=self.global_exercise_name_06,
            description=self.global_exercise_description_06,
            type=self.global_exercise_type_06
        )

        self.global_exercise_07 = Exercise.objects.create(
            name=self.global_exercise_name_07,
            description=self.global_exercise_description_07,
            type=self.global_exercise_type_07
        )

        self.global_exercise_08 = Exercise.objects.create(
            name=self.global_exercise_name_08,
            description=self.global_exercise_description_08,
            type=self.global_exercise_type_08
        )

        self.global_exercise_09 = Exercise.objects.create(
            name=self.global_exercise_name_09,
            description=self.global_exercise_description_09,
            type=self.global_exercise_type_09
        )

        self.global_exercise_10 = Exercise.objects.create(
            name=self.global_exercise_name_10,
            description=self.global_exercise_description_10,
            type=self.global_exercise_type_10
        )

        self.global_exercise_11 = Exercise.objects.create(
            name=self.global_exercise_name_11,
            description=self.global_exercise_description_11,
            type=self.global_exercise_type_11
        )

        self.global_exercise_12 = Exercise.objects.create(
            name=self.global_exercise_name_12,
            description=self.global_exercise_description_12,
            type=self.global_exercise_type_12
        )

        self.global_exercise_13 = Exercise.objects.create(
            name=self.global_exercise_name_13,
            description=self.global_exercise_description_13,
            type=self.global_exercise_type_13
        )

        self.global_exercise_14 = Exercise.objects.create(
        name=self.global_exercise_name_14,
        description=self.global_exercise_description_14,
        type=self.global_exercise_type_14
        )

        self.global_exercise_15 = Exercise.objects.create(
            name=self.global_exercise_name_15,
            description=self.global_exercise_description_15,
            type=self.global_exercise_type_15
        )

        self.global_exercise_16 = Exercise.objects.create(
            name=self.global_exercise_name_16,
            description=self.global_exercise_description_16,
            type=self.global_exercise_type_16
        )

        self.global_exercise_17 = Exercise.objects.create(
            name=self.global_exercise_name_17,
            description=self.global_exercise_description_17,
            type=self.global_exercise_type_17
        )

        self.global_exercise_18 = Exercise.objects.create(
            name=self.global_exercise_name_18,
            description=self.global_exercise_description_18,
            type=self.global_exercise_type_18
        )

        self.global_exercise_19 = Exercise.objects.create(
            name=self.global_exercise_name_19,
            description=self.global_exercise_description_19,
            type=self.global_exercise_type_19
        )

        self.global_exercise_20 = Exercise.objects.create(
            name=self.global_exercise_name_20,
            description=self.global_exercise_description_20,
            type=self.global_exercise_type_20
        )

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



    

    

    
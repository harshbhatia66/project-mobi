from django.test import TestCase
from mobi_app.models import Exercise
# import validation error
from django.core.exceptions import ValidationError
class ExerciseModelTest(TestCase):

    def setUp(self):
        self.exercise_name = "Bench Press"
        self.exercise_description = "A chest exercise involving pushing weight upwards from a bench."
        self.exercise_type = "Chest"
        
        self.exercise = Exercise.objects.create(
            name=self.exercise_name, 
            description=self.exercise_description, 
            type=self.exercise_type
        )

    # Test model instance creation
    def test_model_creation_in_db(self):
        self.assertEqual(Exercise.objects.count(), 1)

    def test_model_creation(self):
        self.assertEqual(self.exercise.name, self.exercise_name)
        self.assertEqual(self.exercise.description, self.exercise_description)
        self.assertEqual(self.exercise.type, self.exercise_type)

    # Test field validations
    def test_name_max_length(self):
        max_length = self.exercise._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    # Test if a name longer than 255 characters is invalid and raises an error
    def test_name_max_length_validation(self):
        exercise_name = "x" * 256
        with self.assertRaises(Exception):
            Exercise.objects.create(
                name=exercise_name, 
                description=self.exercise_description, 
                type=self.exercise_type
            )

    # Test if all fields are required
    

    def test_fields_required(self):
        with self.assertRaises(ValidationError):
            exercise = Exercise(
                description=self.exercise_description, 
                type=self.exercise_type
            )
            exercise.full_clean()

        with self.assertRaises(ValidationError):
            exercise = Exercise(
                name=self.exercise_name, 
                type=self.exercise_type
            )
            exercise.full_clean()

        with self.assertRaises(ValidationError):
            exercise = Exercise(
                name=self.exercise_name, 
                description=self.exercise_description
            )
            exercise.full_clean()



    # Test string representation
    def test_string_representation(self):
        self.assertEqual(str(self.exercise.name), self.exercise_name)

    # Test model field types
    def test_name_field_type(self):
        self.assertEqual(self.exercise._meta.get_field('name').get_internal_type(), 'CharField')
        self.assertEqual(self.exercise._meta.get_field('description').get_internal_type(), 'TextField')
        self.assertEqual(self.exercise._meta.get_field('type').get_internal_type(), 'CharField')


    
    

    
    

    



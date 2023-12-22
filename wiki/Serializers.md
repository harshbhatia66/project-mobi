Requirement: a user can browse through their workout templates, start a workout session, see the exercises from the chosen template, and add sets as part of a session exercise. 

1. **WorkoutTemplateSerializer**:
   - This serializer includes `template_exercises`, which are serialized using `TemplateExerciseSerializer`. It allows users to view all exercises associated with each of their workout templates.

2. **TemplateExerciseSerializer**:
   - Links each `WorkoutTemplate` to its `Exercises` through the `TemplateExercise` model.
   - The `exercise` field uses `ExerciseSerializer`, providing detailed information about each exercise in the template.

3. **WorkoutSessionSerializer**:
   - Represents a workout session. Each session is linked to a user.
   - The `session_exercises` field is serialized using `SessionExerciseSerializer`, showing all exercises that are part of the workout session.

4. **SessionExerciseSerializer**:
   - Links `WorkoutSession` to `Exercise`, showing which exercises are included in a particular session.
   - The `sets` field uses `SetSerializer`, allowing users to view or add sets (including reps, weight, duration) to each exercise during the session.

5. **UserSerializer**:
   - Shows the user's workout sessions (`workout_sessions`), progress records (`user_progress`), and workout templates (`workout_templates`).
   - Each of these fields uses their respective serializers, providing a nested view of the user's related data.

### Functionality Flow

- **Viewing Workout Templates**: Users can view their workout templates, including the exercises in each template.
- **Starting a Workout Session**: When users start a workout session, they can reference their workout templates.
- **Session Exercises and Sets**: During the workout session, users can view the exercises (pulled from the template or added manually) and record their performance in terms of sets.
- **Tracking Progress**: The user's progress over time is tracked and can be viewed through the `UserProgressSerializer`.


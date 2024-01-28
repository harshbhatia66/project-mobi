from django.core.exceptions import ValidationError
from firebase_admin import auth
from django.contrib.auth.models import User
from .models import UserProfile

def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token.get('uid')

        if not uid:
            raise ValidationError('Firebase UID is missing in the token')

        # Check if a UserProfile with this UID already exists
        try:
            user_profile = UserProfile.objects.get(firebase_uid=uid)
            return user_profile.user
        except UserProfile.DoesNotExist:
            # Check if a User with the given username (Firebase UID) exists
            user, user_created = User.objects.get_or_create(username=uid)
            if user_created:
                print('Creating a new user')
            else:
                print('User already exists')

            # Create or link the UserProfile
            user_profile, profile_created = UserProfile.objects.get_or_create(user=user, defaults={'firebase_uid': uid})
            if profile_created:
                print('Creating a new user profile')
            else:
                print('User profile already exists')
            
            return user

    except auth.InvalidIdTokenError:
        print('Invalid Firebase token')
        raise ValidationError('Invalid Firebase token')
    except Exception as e:
        print(f'Error verifying Firebase token: {str(e)}')
        raise ValidationError(f'Error verifying Firebase token: {str(e)}')

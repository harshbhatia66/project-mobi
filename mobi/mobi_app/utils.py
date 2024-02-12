from django.core.exceptions import ValidationError
from django.http import JsonResponse
from firebase_admin import auth
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import boto3
from django.conf import settings

def verify_firebase_token(token):
    try:
        # Decode the Firebase token
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token.get('uid')
        email = decoded_token.get('email')

        # Raise an error if UID is not in the token
        if not uid:
            raise ValidationError('UID is missing in the Firebase token')

        # Check if a User with the given UID already exists
        user, created = User.objects.get_or_create(username=uid, defaults={'email': email})
        if created:
            print('Creating a new user with UID:', uid)
        else:
            print('User with UID already exists:', uid)

        django_token = create_or_get_django_token(user)
        return django_token

    except auth.InvalidIdTokenError:
        print('Invalid Firebase token')
        raise ValidationError('Invalid Firebase token')
    except Exception as e:
        print(f'Error verifying Firebase token: {str(e)}')
        raise ValidationError(f'Error verifying Firebase token: {str(e)}')
    
def create_or_get_django_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token.key



def generate_presigned_url(object_key):
    s3_client = boto3.client('s3',
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                             region_name='ap-southeast-2')  

    presigned_url = s3_client.generate_presigned_url('get_object',
                                                     Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                             'Key': object_key},
                                                     ExpiresIn=3600)  # URL expires in 1 hour
    return presigned_url
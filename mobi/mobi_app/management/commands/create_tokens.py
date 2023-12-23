from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'Generates tokens for all existing users'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Successfully created token for user {user.username}'))

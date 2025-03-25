from django.core.management.base import BaseCommand
from users.models import Account
import random, string


class Command(BaseCommand):
    help = 'Create admin users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
    
    def generate_random_password(self) -> str:
        """Generate a random password.
        """
        length = 10
        symbols = '!@#$%^&*()'
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(symbols),
        ]
        
        password += random.choices(string.ascii_letters + string.digits + symbols, k=length - len(password))
        random.shuffle(password)
        
        return ''.join(password)

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        
        # Generate a strong temporary password
        temp_password = self.generate_random_password()
        
        Account.objects.create_user(
            username=username, 
            email=email, 
            password=temp_password,
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Admin user {username} created. Temporary password: {temp_password}'
            )
        )
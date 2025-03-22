from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User  # or use your custom user model if you have one

class Command(BaseCommand):
    help = 'Send weekly progress report email to all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()  # get all registered users
        for user in users:
            subject = 'Weekly Progress Report'
            message = (
                f'Hello {user.username},\n\n'
                'Here is your weekly progress report:\n'
                'Keep up the good work and stay active!\n\n'
                'Best regards,\n'
                'CUFitness Team'
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
        self.stdout.write(self.style.SUCCESS('Successfully sent weekly progress reports'))

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email="alexander.maslov505@gmail.com",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        user.set_password("121091li")
        user.save()

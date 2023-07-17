from django.core.management import BaseCommand

from app.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email="dmitrymaslov2016@mail.ru",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password("121091li")
        user.save()

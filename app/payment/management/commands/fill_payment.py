from django.core.management import BaseCommand

from app.course.models import Course
from app.payment.models import Payment
from app.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {
                "user": User.objects.get(email="dmitrymaslov2016@mail.ru"),
                "course": Course.objects.get(name="python"),
                "amount": 2000,
                "kind_of_payment": "наличные",
            },
            {
                "user": User.objects.get(email="dmitrymaslov2016@mail.ru"),
                "course": Course.objects.get(name="j"),
                "amount": 4000,
                "kind_of_payment": "перевод",
            },
            {
                "user": User.objects.get(email="alexander.maslov505@gmail.com"),
                "course": Course.objects.get(name="j"),
                "amount": 3000,
                "kind_of_payment": "перевод",
            },
            {
                "user": User.objects.get(email="alexander.maslov505@gmail.com"),
                "course": Course.objects.get(name="python"),
                "amount": 3000,
                "kind_of_payment": "наличные",
            },
        ]

        payment_for_create = []

        for payment in payment_list:
            payment_for_create.append(Payment(**payment))

        Payment.objects.bulk_create(payment_for_create)

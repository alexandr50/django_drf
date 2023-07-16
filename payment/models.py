from django.db import models

from course.models import Course
from lesson.models import Lesson
from users.models import User


class Payment(models.Model):
    KIND_OF_PAYMENT = (
        ('Cash', 'наличные'),
        ('Tranfer', 'перевод')
    )

    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='пользователь')
    date_pay = models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name='сумма платежа')
    kind_of_payment = models.CharField(choices=KIND_OF_PAYMENT, verbose_name='вид платежа')

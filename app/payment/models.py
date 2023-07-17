from django.contrib.auth import get_user_model
from django.db import models


class Payment(models.Model):
    KIND_OF_PAYMENT = (
        ("Cash", "наличные"),
        ("Tranfer", "перевод"),
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.RESTRICT,
        verbose_name="пользователь",
    )
    date_pay = models.DateTimeField(auto_now_add=True, verbose_name="дата платежа")
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        verbose_name="курс",
        blank=True,
        null=True,
    )
    lesson = models.ForeignKey(
        "lesson.Lesson",
        on_delete=models.CASCADE,
        verbose_name="урок",
        blank=True,
        null=True,
    )
    amount = models.PositiveIntegerField(verbose_name="сумма платежа")
    kind_of_payment = models.CharField(
        choices=KIND_OF_PAYMENT,
        verbose_name="вид платежа",
    )

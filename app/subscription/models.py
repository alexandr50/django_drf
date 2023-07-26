from django.contrib.auth import get_user_model
from django.db import models


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="подписка")
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        verbose_name="курс",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )

    def __str__(self):
        return f"{self.user} | {self.course.name}"

    # def save(self, *args, **kwargs):
    #     user = self.user
    #     super().save(*args, **kwargs)

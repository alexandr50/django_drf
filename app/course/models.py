from django.db import models


class Course(models.Model):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="создатель",
    )
    name = models.CharField(max_length=30, verbose_name="название")
    preview = models.ImageField(
        upload_to="course",
        verbose_name="превью",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="описание")
    url = models.URLField(max_length=30, default="youtube.com", verbose_name="ссылка")
    price = models.PositiveIntegerField(default=3000, verbose_name='стоимость курса')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

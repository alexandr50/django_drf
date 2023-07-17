from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name="название")
    preview = models.ImageField(
        upload_to="course",
        verbose_name="превью",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=30, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    preview = models.ImageField(upload_to="lesson", blank=True, null=True)
    url = models.URLField(max_length=30, verbose_name="ссылка")
    course = models.ManyToManyField("course.Course", verbose_name="курс")
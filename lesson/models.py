from django.db import models

from course.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson', blank=True, null=True)
    url = models.CharField(max_length=30, verbose_name='ссылка')
    course = models.ManyToManyField(Course, verbose_name='курс', blank=True, null=True)

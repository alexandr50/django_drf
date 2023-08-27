# Generated by Django 4.2.3 on 2023-07-18 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_course_owner'),
        ('lesson', '0004_alter_lesson_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(to='course.course', verbose_name='курс'),
        ),
    ]

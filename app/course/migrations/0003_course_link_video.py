# Generated by Django 4.2.3 on 2023-07-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link_video',
            field=models.URLField(default='youtube.com', max_length=30, verbose_name='ссылка'),
        ),
    ]
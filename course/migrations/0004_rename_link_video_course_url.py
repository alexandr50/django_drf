# Generated by Django 4.2.3 on 2023-07-21 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_link_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='link_video',
            new_name='url',
        ),
    ]

#
# import json
# from datetime import datetime, timedelta
#
# from celery.schedules import schedule
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
#
# def set_shedule(*args, **kwargs):
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=1,
#         period=IntervalSchedule.SECONDS,
#
#     )
#
#     PeriodicTask.objects.create(
#         interval=schedule,
#         name='Check last login',
#         task='users.tasks.check_last_login',
#         args=json.dumps(['arg1', 'arg2']),
#         kwargs=json.dumps({
#             'be_careful': True,
#         }),
#         expires=datetime.utcnow() + timedelta(seconds=30)
#
#     )

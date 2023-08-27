from celery import shared_task
from django.core.mail import send_mail

from config import settings
from course.models import Course
from subscription.models import Subscription


@shared_task
def check_change_course(course_id, date_last, date_updated):
    instance = Course.objects.get(id=course_id)
    emails_list = list(set([us.user.email for us in Subscription.objects.filter(course_id=instance.id)
                            if us.is_active == True]))
    if date_last != date_updated:
        send_mail(
            subject='Обновление',
            message='Посмотрите, наш курс обновился',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.PASSWORD_YANDEX,
        )


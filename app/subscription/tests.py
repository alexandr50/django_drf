from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course
from subscription.models import Subscription
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='testing@mail.ru'
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            owner=self.user,
            name='Тестовый курс',
            description='Описание тестового курса',
            url='https://youtube.com',
        )


    def test_subscription_create(self):
        data = {
            'course': self.course.id,
            'is_active': True

        }

        response = self.client.post(f'/api/v1/subscriptions/create/', data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Subscription.objects.all().count(), 1)
        self.assertEquals(Subscription.objects.get(course=self.course.id).user, self.user)
        self.assertTrue(Subscription.objects.get(course=self.course.id).is_active, True)

    def test_subscription_delete(self):
        data = {
            'course': self.course,
            'is_active': True,
            "user": self.user

        }
        sub = Subscription.objects.create(**data)

        response = self.client.delete(f'/api/v1/subscriptions/delete/{sub.id}/')

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Subscription.objects.all().count(), 0)

from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from lesson.models import Lesson

from users.models import User


class LessonsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="testing@mail.ru",
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            owner=self.user,
            name="Тестовый курс",
            description="Описание тестового курса",
            url="https://youtube.com",
        )

    def test_create_lesson(self):
        data = {
            "owner": 1,
            "name": "name",
            "description": "description",
            "url": "https://youtube.com",
            "course": 1,
        }

        response = self.client.post(
            "/api/v1/lessons/create/",
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Lesson.objects.count(), 1)
        self.assertEqual(Lesson.objects.get().name, "name")

    def test_delete_lesson(self):
        data = {
            "owner": self.user,
            "name": "name",
            "description": "description",
            "url": "https://youtube.com",
        }

        lesson = Lesson.objects.create(**data)
        lesson.course.add(self.course)

        response = self.client.delete(f"/api/v1/lessons/delete/{lesson.id}/")

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertEqual(Lesson.objects.all().count(), 0)
        self.assertFalse(Lesson.objects.filter(id=lesson.id).exists())

    def test_get_lesson(self):
        data = {
            "owner": self.user,
            "name": "name",
            "description": "description",
            "url": "https://youtube.com",
        }

        lesson = Lesson.objects.create(**data)
        lesson.course.add(self.course)

        response = self.client.get(
            f"/api/v1/lessons/",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Lesson.objects.get().name, "name")

    def test_update_lesson(self):
        data = {
            "owner": self.user,
            "name": "name",
            "description": "description",
            "url": "https://youtube.com",
        }

        lesson = Lesson.objects.create(**data)
        lesson.course.add(self.course)

        data_for_update = {
            "owner": self.user.id,
            "name": "name_update",
            "description": "description",
            "url": "https://youtube.com",
            "course": self.course.id,
        }

        response = self.client.put(
            f"/api/v1/lessons/update/{lesson.id}/",
            data_for_update,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Lesson.objects.get().name, "name_update")

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from course.pagination import PaginationsCourse
from lesson.serializers import LessonSerializer
from users.permissions import IsModerator
from lesson.models import Lesson


class LessonList(ListAPIView):
    """Вью возвращающая список уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]
    pagination_class = PaginationsCourse


class LessonCreate(CreateAPIView):
    """Вью создающая урок"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonUpdate(UpdateAPIView):
    """Вью обновляющая урок"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsModerator]


class LessonDelete(DestroyAPIView):
    """Вью удаляющая урок"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsModerator]


class LessonDetail(RetrieveAPIView):
    """Вью возвращающая урок"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]

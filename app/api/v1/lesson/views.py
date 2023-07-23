from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from api.v1.course.pagination import PaginationsCourse
from api.v1.lesson.serializers import LessonSerializer
from api.v1.users.permissions import IsModerator
from lesson.models import Lesson


class LessonList(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]
    pagination_class = PaginationsCourse


class LessonCreate(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]


class LessonUpdate(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsModerator]


class LessonDelete(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsModerator]


class LessonDetail(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]

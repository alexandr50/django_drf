from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from api.v1.lesson.serializers import LessonSerializer
from lesson.models import Lesson



class LessonList(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreate(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdate(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDelete(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()





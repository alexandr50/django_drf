from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from lesson.models import Lesson
from lesson.serializers import LessonSerializer


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





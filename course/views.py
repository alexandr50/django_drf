from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer


class CourseLViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

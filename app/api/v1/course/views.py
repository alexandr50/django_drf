from rest_framework import viewsets

from api.v1.course import CourseSerializer
from course.models import Course



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

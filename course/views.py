from rest_framework import viewsets
from rest_framework.response import Response

from course.pagination import PaginationsCourse
from course.serializers import CourseSerializer
from course.tasks import check_change_course
from course.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    # permission_classes = [IsModerator]
    pagination_class = PaginationsCourse

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)


    def perform_update(self, serializer):
        instance = self.get_object()
        updated_inctance = serializer.save(owner=self.request.user)
        updated_inctance.owner = self.request.user

        check_change_course.delay(instance.id, instance.updated_at, updated_inctance.updated_at)
        updated_inctance.save()



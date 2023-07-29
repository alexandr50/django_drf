from rest_framework import viewsets

from api.v1.course import CourseSerializer
from api.v1.course.pagination import PaginationsCourse
from api.v1.course.tasks import check_change_course
from api.v1.users.permissions import IsModerator
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
        check_change_course.delay(instance, updated_inctance)


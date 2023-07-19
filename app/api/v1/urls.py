from django.conf import settings
from django.urls import include, path

from rest_framework.routers import DefaultRouter, SimpleRouter

from api.v1.course import CourseViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("courses", CourseViewSet, basename='courses')

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("api.v1.lesson.urls")),
    path("v1/", include("api.v1.payment.urls")),
    path("v1/", include("api.v1.users.urls")),
]

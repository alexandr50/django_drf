from django.urls import path
from lesson import apps


from lesson.views import (
    LessonList,
    LessonCreate,
    LessonUpdate,
    LessonDelete,
    LessonDetail,
)

app_name = apps.LessonConfig.name

urlpatterns = [
    path("", LessonList.as_view(), name="list_view"),
    path("create/", LessonCreate.as_view(), name="create_view"),
    path("update/<int:pk>/", LessonUpdate.as_view(), name="update_view"),
    path("delete/<int:pk>/", LessonDelete.as_view(), name="delete_view"),
    path("detail/<int:pk>/", LessonDetail.as_view(), name="delete_view"),
]

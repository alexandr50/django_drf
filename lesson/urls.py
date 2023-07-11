from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import LessonList, LessonCreate, LessonUpdate, LessonDelete

app_name = LessonConfig.name

urlpatterns = [

    path('', LessonList.as_view(), name='list_view'),
    path('create/', LessonCreate.as_view(), name='create_view'),
    path('update/<int:pk>/', LessonUpdate.as_view(), name='update_view'),
    path('delete/<int:pk>/', LessonDelete.as_view(), name='delete_view'),

]
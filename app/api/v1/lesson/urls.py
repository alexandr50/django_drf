from django.urls import path


from app.api.v1.lesson.views import LessonList, LessonCreate, LessonUpdate, LessonDelete



urlpatterns = [

    path('lessons/', LessonList.as_view(), name='list_view'),
    path('lessons/create/', LessonCreate.as_view(), name='create_view'),
    path('lessons/update/<int:pk>/', LessonUpdate.as_view(), name='update_view'),
    path('lessons/delete/<int:pk>/', LessonDelete.as_view(), name='delete_view'),

]

from django.urls import path

from users.apps import UsersConfig
from users.views import UsersList, UserCreate, UserUpdate, UserDelete

app_name = UsersConfig.name

urlpatterns = [

    path('', UsersList.as_view(), name='list_view'),
    path('create/', UserCreate.as_view(), name='create_view'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='update_view'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='delete_view'),

]
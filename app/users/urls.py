from django.urls import path

from app.users.apps import UsersConfig
from app.users.views import (
    UsersListAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    UserDetailAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersListAPIView.as_view(), name="list_view"),
    path("create/", UserCreateAPIView.as_view(), name="create_view"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_view"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete_view"),
    path("detail/<int:pk>/", UserDetailAPIView.as_view(), name="detail_view"),
]

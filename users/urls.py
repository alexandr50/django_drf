from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UsersListAPIView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    UserDetailAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", UsersListAPIView.as_view(), name="list_view"),
    path("create/", UserCreateAPIView.as_view(), name="create_view"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="update_view"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="delete_view"),
    path("detail/<int:pk>/", UserDetailAPIView.as_view(), name="detail_view"),
]

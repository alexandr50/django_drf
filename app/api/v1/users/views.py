from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)

from users.models import User
from api.v1.users.serializers import UserSerializers, UserDetailSerializer


class UsersListAPIView(ListAPIView):
    """Вью возвращающая список пользователей"""

    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    """Вью создающая пользователя"""

    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """Вью обновляющая пользователя"""

    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    """Вью удаляющая пользователя"""

    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    """Вью возвращающая пользователя"""

    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

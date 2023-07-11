from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserSerializers


class UsersList(ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()

class UserCreate(CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()

class UserUpdate(UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()

class UserDelete(DestroyAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


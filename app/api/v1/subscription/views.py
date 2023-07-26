from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from api.v1.subscription.serializers import (
    SubscriptionSerializer,
    SubscriptionCreateSerializer,
)
from subscription.models import Subscription


class SubscriptionList(ListAPIView):
    """Вью возвращающая список подписок"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionCreate(CreateAPIView):
    """Вью создающая подписку"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializer


class SubscriptionDelete(DestroyAPIView):
    """Вью удаляющая подписку"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

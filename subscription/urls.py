from django.urls import path
from subscription import apps

from subscription.views import (
    SubscriptionCreate,
    SubscriptionDelete,
    SubscriptionList,
)

app_name = apps.SubscriptionConfig.name

urlpatterns = [
    path("", SubscriptionList.as_view(), name="list_view"),
    path("create/", SubscriptionCreate.as_view(), name="create_view"),
    path(
        "delete/<int:pk>/",
        SubscriptionDelete.as_view(),
        name="delete_view",
    ),
]

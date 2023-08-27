from django.urls import path

from payment.apps import PaymentConfig
from payment.views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentDeleteAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
)

app_name = PaymentConfig.name

urlpatterns = [
    path("", PaymentListAPIView.as_view(), name="list_view"),
    path("create/", PaymentCreateAPIView.as_view(), name="create_view"),
    path(
        "update/<int:pk>/",
        PaymentUpdateAPIView.as_view(),
        name="update_view",
    ),
    path(
        "delete/<int:pk>/",
        PaymentDeleteAPIView.as_view(),
        name="delete_view",
    ),
    path(
        "detail/<int:pk>/",
        PaymentDetailAPIView.as_view(),
        name="detail_view",
    ),
]

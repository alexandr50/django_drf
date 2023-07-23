from django.urls import path

from app.payment.apps import PaymentConfig
from app.api.v1.payment.views import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymentDeleteAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
)

app_name = PaymentConfig.name

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view(), name="list_view"),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="create_view"),
    path(
        "payments/update/<int:pk>/",
        PaymentUpdateAPIView.as_view(),
        name="update_view",
    ),
    path(
        "payments/delete/<int:pk>/",
        PaymentDeleteAPIView.as_view(),
        name="delete_view",
    ),
    path(
        "payments/detail/<int:pk>/",
        PaymentDetailAPIView.as_view(),
        name="detail_view",
    ),
]

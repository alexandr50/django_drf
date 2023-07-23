from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from api.v1.payment.serializers import PaymentSerializers
from payment.models import Payment


class PaymentBaseAPIView:
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentListAPIView(PaymentBaseAPIView, generics.ListAPIView):
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("course", "kind_of_payment")
    ordering_fields = ("date_pay",)


class PaymentCreateAPIView(PaymentBaseAPIView, generics.CreateAPIView):
    pass


class PaymentUpdateAPIView(PaymentBaseAPIView, generics.UpdateAPIView):
    pass


class PaymentDeleteAPIView(PaymentBaseAPIView, generics.DestroyAPIView):
    pass


class PaymentDetailAPIView(PaymentBaseAPIView, generics.RetrieveAPIView):
    pass

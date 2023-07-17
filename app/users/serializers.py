from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app.payment import Payment
from app.users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):

    payments = SerializerMethodField()

    def get_payments(self, user):
        return [(el.date_pay, el.amount) for el in Payment.objects.filter(user=user)]

    class Meta:
        model = User
        fields = ("email", "phone", "city", "payments")

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


from users.models import User
from payment.models import Payment


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "city")


class UserDetailSerializer(serializers.ModelSerializer):

    payments = SerializerMethodField()

    def get_payments(self, user):
        return [(el.date_pay, el.amount) for el in Payment.objects.filter(user=user)]

    class Meta:
        model = User
        fields = ("email", "phone", "city", "payments")

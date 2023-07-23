from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    def get_user(self, subscription):
        return User.objects.get(subscription=subscription).email

    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        fields = '__all__'


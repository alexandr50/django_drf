from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.v1.course.validators import UrlValidate
from lesson.models import Lesson
from course.models import Course
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

    def get_lessons(self, course):
        return [el.name for el in Lesson.objects.filter(course=course)]

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = "__all__"
        validators = [UrlValidate(value="link_video")]

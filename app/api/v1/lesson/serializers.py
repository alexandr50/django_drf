from rest_framework import serializers

from api.v1.course.validators import UrlValidate
from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidate(value="url")]

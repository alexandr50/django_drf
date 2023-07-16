from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lesson.models import Lesson
from .models import Course

class CourseSerializer(serializers.ModelSerializer):

    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()
    def get_lessons(self, course):
        return [el.name for el in Lesson.objects.filter(course=course)]
    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'
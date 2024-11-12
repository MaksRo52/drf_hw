from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import validate_lesson_video_link


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
       return [lesson.title for lesson in Lesson.objects.filter(course=obj)]

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_lesson_video_link])
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True)

    def get_count_lessons(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'image','count_lessons', 'lesson')


from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'image','count_lessons')



class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
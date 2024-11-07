from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    def get_lessons(self, obj):
       return [lesson.title for lesson in Lesson.objects.filter(course=obj)]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_count_lessons(self, obj):
        return obj.lesson_set.count()

    def get_lessons(self, obj):
       return [lesson.title for lesson in Lesson.objects.filter(course=obj)]

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'image','count_lessons', 'lessons')



class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
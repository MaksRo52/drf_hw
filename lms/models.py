from django.db import models

NULLABLE = {"blank": True, "null": True}

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.SET_NULL, related_name='lesson', **NULLABLE)
    title = models.CharField(max_length=200, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на урок', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

from django.conf import settings
from django.db import models


NULLABLE = {"blank": True, "null": True}

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, **NULLABLE)
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата подписки')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

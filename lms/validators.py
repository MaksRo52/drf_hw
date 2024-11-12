from rest_framework.exceptions import ValidationError


def validate_lesson_video_link(value):
    """Проверяет, является ли переданная строка ссылкой на видео youtube.com."""
    if "youtube.com" not in value.lower():
        raise ValidationError("Ссылки на сторонние материалы прикреплять нельзя")
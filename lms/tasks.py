from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_information_from_subscribe(course, email):
    send_mail(
        "Сообщение о подписке",
        f"Был обновлен курс: {course}",
        settings.EMAIL_HOST_USER,
        [email],
    )
    print(f"Письмо отправлено на адрес {email} о обновлении курса: {course}")
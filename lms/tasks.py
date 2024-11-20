from datetime import timedelta, timezone

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import User


@shared_task
def send_information_from_subscribe(course, email):
    send_mail(
        "Сообщение о подписке",
        f"Был обновлен курс: {course}",
        settings.EMAIL_HOST_USER,
        [email],
    )
    print(f"Письмо отправлено на адрес {email} о обновлении курса: {course}")

@shared_task
def block_user():
    now = timezone.now()
    users = User.objects.filter(last_login__lte=now - timedelta(days=30), is_active=True)
    for user in users:
        user.is_active = False
        user.save()
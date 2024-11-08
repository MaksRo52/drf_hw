from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment = Payment.objects.create()
        payment.user_id = "test"
        payment.course("Тестовый Курс2")
        payment.payment_method("transfer")
        payment.save()

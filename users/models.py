from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from lms.models import Course, Lesson, NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = PhoneNumberField(
        null=True, blank=True, verbose_name="Номер телефона"
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", null=True, blank=True
    )
    photo = models.ImageField(
        upload_to="users/photos/",
        verbose_name="Фото",
        help_text="Загрузите своё фото.",
        null=True,
        blank=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен", null=True, blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("can_edit_is_active", "Может блокировать пользователя"),
            ("can_view_users", "Может просматривать пользователей"),
        ]

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    amount = models.DecimalField(
        verbose_name="Сумма оплаты", max_digits=10, decimal_places=2,
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Оплаченный курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name="Оплаченный урок", **NULLABLE)
    payment_method = models.CharField(max_length=20, choices={"cash": "Оплата наличными", "transfer": "Оплата переводом"})

from django.contrib import admin

from users.models import User, Payment


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "token")

@admin.register(Payment)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "amount")
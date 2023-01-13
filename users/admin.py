from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "last_login")

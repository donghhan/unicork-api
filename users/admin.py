from datetime import date, datetime
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = "-- ไม่มีข้อมูล --"
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "mobile_phone_number",
        "last_login_time_in_buddhism",
    )

    @admin.display(description="เข้าสู่ระบบครั้งล่าสุด")
    def last_login_time_in_buddhism(self, obj):
        if obj.last_login:
            return f"{obj.last_login.day} / {obj.last_login.month} / {obj.last_login.year + 544} {obj.last_login.hour}:{obj.last_login.minute}"
        else:
            return "ไม่ทราบ"

    list_filter = ("is_admin",)
    readonly_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "mobile_phone_number",
        "last_login_time_in_buddhism",
    )
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    search_help_text = "ค้นหาได้จาก ID, อีเมล, ชื่อและนามสกุล."

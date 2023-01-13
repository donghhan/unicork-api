from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, password=None):
        if not username:
            raise ValueError("คุณควรระบุชื่อผู้ใช้.")
        if not email:
            raise ValueError("คุณควรระบุอีเมล.")
        if not first_name:
            raise ValueError("คุณควรระบุชื่อ.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, password=None):
        user = self.create_user(
            username=username, email=email, first_name=first_name, password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, verbose_name="ID", unique=True)
    email = models.EmailField(max_length=150, verbose_name="E-mail")
    mobile_phone_number = models.CharField(max_length=200, verbose_name="เบอร์โทรศัพท์")
    first_name = models.CharField(max_length=150, verbose_name="ชื่อ")
    last_name = models.CharField(max_length=150, verbose_name="นามสกุล", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="ผู้ใช้ที่ใช้งานอยู่")
    is_admin = models.BooleanField(default=False, verbose_name="ผู้ดูแลระบบ")

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        if self.is_admin:
            return True
        else:
            return False

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "ผู้ใช้"
        verbose_name_plural = "ผู้ใช้"
        db_table = "user"

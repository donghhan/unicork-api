# Generated by Django 4.1.5 on 2023-01-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('mobile_phone_number', models.CharField(max_length=200, verbose_name='เบอร์โทรศัพท์')),
                ('first_name', models.CharField(max_length=150, verbose_name='ชื่อ')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='นามสกุล')),
                ('is_active', models.BooleanField(default=True, verbose_name='ผู้ใช้ที่ใช้งานอยู่')),
            ],
            options={
                'verbose_name': 'ผู้ใช้',
                'verbose_name_plural': 'ผู้ใช้',
                'db_table': 'user',
            },
        ),
    ]
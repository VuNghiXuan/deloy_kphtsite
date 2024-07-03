# Generated by Django 5.0.4 on 2024-06-19 22:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Họ và tên')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Số điện thoại')),
                ('bank_account', models.CharField(blank=True, max_length=20, verbose_name='Tài khoản ngân hàng')),
                ('id_card', models.CharField(blank=True, max_length=20, verbose_name='Căn cước công dân')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('address', models.CharField(max_length=255, verbose_name='Địa chỉ')),
                ('address_get', models.CharField(max_length=255, verbose_name='Địa chỉ nhận hàng')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Mã khách hàng')),
            ],
            options={
                'verbose_name_plural': 'Địa chỉ giao hàng',
            },
        ),
    ]

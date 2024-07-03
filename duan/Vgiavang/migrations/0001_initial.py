# Generated by Django 5.0.4 on 2024-05-19 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IIIquanlykho', '0012_alter_nhaphang_nhom_hang'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiaVang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_thu_tu', models.CharField(blank='', editable=False, max_length=10, verbose_name='STT')),
                ('kich_hoat', models.BooleanField(blank='', default=True, verbose_name='Kích hoạt')),
                ('gia_vang', models.IntegerField(default=0, verbose_name='Giá vàng')),
                ('loai_vang', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gia_vangs', to='IIIquanlykho.loaivang', verbose_name='Loại vàng')),
            ],
            options={
                'verbose_name': 'Cập nhật giá vàng',
                'verbose_name_plural': '1. Cập nhật giá vàng',
            },
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-19 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vgiavang', '0003_giavang_gia_vang_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giavang',
            name='gia_vang_1',
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIIquanlykho', '0014_nhaphang_cong_ban_nhaphang_cong_von_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhaphang',
            name='so_lo',
            field=models.CharField(default='', max_length=50, verbose_name='Số lô'),
            preserve_default=False,
        ),
    ]
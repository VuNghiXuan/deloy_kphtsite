# Generated by Django 5.0.4 on 2024-05-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIIquanlykho', '0006_nhacungcap_nhaphang_ma_san_pham_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhaphang',
            name='ma_vach',
            field=models.ImageField(blank=True, editable=False, upload_to='ma_vach', verbose_name='Mã vạch'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-06-20 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VIIItratien', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='shipping_address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address_get',
            new_name='shipping_address_get',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='bank_account',
            new_name='shipping_bank_account',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='email',
            new_name='shipping_email',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='id_card',
            new_name='shipping_id_card',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='phone',
            new_name='shipping_phone',
        ),
    ]

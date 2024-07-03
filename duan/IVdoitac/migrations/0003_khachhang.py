# Generated by Django 5.0.4 on 2024-05-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IVdoitac', '0002_rename_ten_nha_cung_cap_nhacungcap_nha_cung_cap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_thu_tu', models.CharField(blank='', editable=False, max_length=10, verbose_name='STT')),
                ('kich_hoat', models.BooleanField(blank='', default=True, verbose_name='Kích hoạt')),
                ('ho_ten', models.CharField(max_length=255, verbose_name='Họ và tên')),
                ('sdt', models.CharField(max_length=15, verbose_name='Số điện thoại')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('mat_khau', models.CharField(max_length=100, verbose_name='Mật khẩu')),
                ('so_cccd', models.CharField(max_length=100, verbose_name='Số căn cước')),
                ('dia_chi', models.CharField(max_length=100, verbose_name='Địa chỉ')),
                ('anh_dai_dien', models.ImageField(blank=True, null=True, upload_to='khach/%Y/%m', verbose_name='Ảnh đại diện')),
                ('anh_cccd', models.ImageField(blank=True, null=True, upload_to='cancuoc/%Y/%m', verbose_name='Ảnh chụp căn cước')),
                ('diem', models.IntegerField(default=0, editable=False, verbose_name='Điểm tích lũy')),
            ],
            options={
                'verbose_name': 'Khách hàng',
                'verbose_name_plural': '4. Khách hàng',
            },
        ),
    ]

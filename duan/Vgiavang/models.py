from django.db import models
from Ithongtincongty.models import LopCoBan
from IIIquanlykho.models import LoaiVang
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.



# Định dạng thủ công thay cho settings
# from django.utils import number_format
# number = 12055398187549
# formatted_number = number_format.format(number, grouping=3)
# print(formatted_number)


class GiaVang(LopCoBan): 
    loai_vang = models.OneToOneField(LoaiVang, on_delete=models.SET_NULL, null=True, verbose_name="Loại vàng", related_name='gia_vangs', default=1)   
    # loai_vang = models.ForeignKey(LoaiVang, on_delete=models.SET_NULL, null=True, verbose_name="Loại vàng", related_name='gia_vangs', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    # gia_mua = models.IntegerField(verbose_name="Giá mua", default=0)
    gia_mua = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Giá mua") 
    # gia_mua = models.IntegerField(verbose_name="Giá mua", default=0, widget=forms.TextInput(attrs={'size': 10, 'maxlength': 20}))
    gia_ban = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Giá bán") 
    # gia_ban = models.IntegerField(verbose_name="Giá bán", default=0) 
    
    class Meta:
        verbose_name = "Cập nhật giá vàng"
        verbose_name_plural = "1. Cập nhật giá vàng"
    
    def __str__(self):
        return self.loai_vang.ten_loai_vang  # Assuming 'ten_loai_vang' is the name field in LoaiVang

    # @property
    # def formatted_gia_vang(self):
    #     return '{:,}'.format(self.gia_vang).replace(',', '.')

    class Meta:
        verbose_name = "Cập nhật giá vàng"
        verbose_name_plural = "1. Cập nhật giá vàng"

@receiver(post_delete, sender=GiaVang)
def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

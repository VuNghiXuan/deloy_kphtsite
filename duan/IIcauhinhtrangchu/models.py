from django.db import models
from Ithongtincongty.models import LopCoBan
from django.db.models.signals import post_delete
from django.dispatch import receiver
# from django.db.models.signals import pre_save

class BoSuuTap(LopCoBan):
    ten_bo_suu_tap = models.CharField(max_length=100, verbose_name= "Tên bộ sưu tập", unique=True)
    anh_dai_dien = models.ImageField(upload_to="bo_suu_tap", verbose_name = "Tải ảnh đại diện")
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.CASCADE, related_name='phong_bans', verbose_name=_("Thuộc chi nhánh"), default=1)

    class Meta:
        verbose_name ="Bộ sưu tập"
        verbose_name_plural = "1. Bộ sưu tập"
        

    def __str__(self):
        return self.ten_bo_suu_tap


@receiver(post_delete, sender=BoSuuTap)
# @receiver(post_delete, sender=SanPham)


def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

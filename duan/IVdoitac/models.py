from django.db import models
from Ithongtincongty.models import LopCoBan
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class NhaCungCap(LopCoBan):
    
    nha_cung_cap = models.CharField(max_length=255, verbose_name="Nhà cung cấp", unique=True)
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc chi nhánh", related_name='quay_lons', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    # # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='phong_bans', default=1)  # Relates to ChiNhanh# on_delete=models.CASCADE,
    
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    class Meta:
        verbose_name = "Nhà cung cấp"
        verbose_name_plural = "1. Nhà cung cấp"
    
    def __str__(self):
        return self.nha_cung_cap
    
class NhaVanChuyen(LopCoBan):    
    nha_van_chuyen = models.CharField(max_length=255, verbose_name="Nhà vận chuyển", unique=True)
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc chi nhánh", related_name='quay_lons', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    # # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='phong_bans', default=1)  # Relates to ChiNhanh# on_delete=models.CASCADE,
    
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    class Meta:
        verbose_name = "Nhà vận chuyển"
        verbose_name_plural = "2. Nhà vận chuyển"
    
    def __str__(self):
        return self.nha_van_chuyen
    
class ThoNgoai(LopCoBan):    
    ten_tho = models.CharField(max_length=255, verbose_name="Tên thợ", unique=True)
    # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True,  verbose_name="Thuộc chi nhánh", related_name='quay_lons', default=1)#related_name='ten_quay_lons', to_field='ten_chi_nhanh',
    # # chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.SET_NULL, null=True, related_name='phong_bans', default=1)  # Relates to ChiNhanh# on_delete=models.CASCADE,
    
    # hoat_dong = models.BooleanField(verbose_name="Hoạt động", default=True)
    class Meta:
        verbose_name = "Thợ ngoài"
        verbose_name_plural = "3. Thợ ngoài"
    
    def __str__(self):
        return self.ten_tho


class KhachHang(LopCoBan):    
    ho_ten = models.CharField(max_length=255, verbose_name="Họ và tên")
    sdt = models.CharField(max_length=15, verbose_name="Số điện thoại")
    email = models.EmailField(max_length=100, verbose_name="Email", null=True, blank=True)
    mat_khau = models.CharField(max_length=100, verbose_name="Mật khẩu")
    so_cccd = models.CharField(max_length=100, verbose_name="Số căn cước")
    dia_chi = models.CharField(max_length=100, verbose_name="Địa chỉ")
    anh_dai_dien = models.ImageField(upload_to="khach/%Y/%m", verbose_name = "Tải ảnh đại diện", null=True, blank=True)
    anh_cccd = models.ImageField(upload_to="cancuoc/%Y/%m", verbose_name = "Ảnh chụp căn cước", null=True, blank=True)
    diem = models.IntegerField(verbose_name="Điểm tích lũy", default=0, editable=False) 
    
    class Meta:
        verbose_name = "Khách hàng"
        verbose_name_plural = "4. Khách hàng"
    
    def __str__(self):
        return self.ho_ten
    


@receiver(post_delete, sender=NhaCungCap)
@receiver(post_delete, sender=NhaVanChuyen)
@receiver(post_delete, sender=ThoNgoai)
@receiver(post_delete, sender=KhachHang)


def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

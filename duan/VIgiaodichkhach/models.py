from django.db import models
# import barcode 
# from barcode.writer import ImageWriter
# from io import BytesIO
# from django.core.files import File
# from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save

from Ithongtincongty.models import LopCoBan, ChiNhanh
from IVdoitac.models import NhaCungCap, KhachHang
from IIIquanlykho.models import NhapHang

class LoaiGiaoDich(LopCoBan):
    ten_giao_dich = models.CharField(max_length=255, verbose_name='Tên giao dịch')
    class Meta:
        verbose_name = "Danh mục giao dịch"
        verbose_name_plural = "1. Danh mục giao dịch"

    def __str__(self):
        return self.ten_giao_dich



class DonHang(LopCoBan):
    trang_thai_don_hang_choices = (
        ("cho_xu_ly", "Chờ xử lý"),
        ("da_xac_nhan", "Đã xác nhận"),
        ("dang_giao_hang", "Đang giao hàng"),
        ("da_hoan_thanh", "Đã hoàn thành"),
        ("da_huy", "Đã hủy"),
    )
    loai_giao_dich = models.ManyToManyField(LoaiGiaoDich, through='DonHangLoaiGiaoDich')

    # loai_giao_dich = models.ForeignKey(LoaiGiaoDich, on_delete=models.CASCADE, default=1, verbose_name='Loại giao dịch')
    ngay_tao = models.DateTimeField(auto_created=True, verbose_name='Ngày tạo', null=True, editable=False)
    nhan_vien = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Nhân viên')
    khach_hang = models.ForeignKey('IVdoitac.KhachHang', on_delete=models.CASCADE, verbose_name='Khách hàng')  # Assuming 'IVdoitac.KhachHang' for customer model
    chi_nhanh = models.ForeignKey('Ithongtincongty.ChiNhanh', on_delete=models.CASCADE, default=1, verbose_name='Chi nhánh')  # Assuming 'Ithongtincongty.ChiNhanh' for branch model

    # Consider using a ManyToManyField for selecting multiple products
    # ten_san_pham = models.ForeignKey(NhapHang.ten_san_pham, on_delete=models.CASCADE)
    san_pham = models.ManyToManyField(NhapHang, through='DonHangChiTiet', verbose_name='Sản phẩm')

    trang_thai_don_hang = models.CharField(
        max_length=20, choices=trang_thai_don_hang_choices, default="cho_xu_ly", verbose_name="Trạng thái đơn hàng"
    )
    tong_gia_tri = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="Tổng giá trị")
    tam_ung = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='Số tiền tạm ứng')
    so_tien_con_lai = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='Số tiền còn lại')


    phuong_thuc_thanh_toan = models.CharField(max_length=50, verbose_name="Phương thức thanh toán", blank=True)
    ghi_chu = models.TextField(blank=True, verbose_name="Ghi chú")

    class Meta:
        verbose_name = "Đơn hàng"
        verbose_name_plural = "2. Đơn hàng"
    
    def save(self, *args, **kwargs):
        # Cập nhật `so_tien_con_lai` khi lưu đơn hàng
        self.so_tien_con_lai = self.tong_gia_tri - self.tam_ung
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Đơn hàng {self.id} - {self.khach_hang}"
    
class DonHangLoaiGiaoDich(LopCoBan):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE, verbose_name='Đơn hàng')
    loai_giao_dich = models.ForeignKey(LoaiGiaoDich, on_delete=models.CASCADE, verbose_name='Chọn giao dịch')

    class Meta:
        verbose_name = "Đơn hàng - Loại giao dịch"
        verbose_name_plural = "2a. Đơn hàng - Loại giao dịch"



from .check_hang_ton import validate_stock    
class DonHangChiTiet(LopCoBan):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE, verbose_name="Đơn hàng")
    nhap_hang = models.ForeignKey(NhapHang, on_delete=models.CASCADE, verbose_name="Nhập hàng")
    so_luong = models.PositiveIntegerField(verbose_name="Số lượng")
    don_gia = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Đơn giá")
    thanh_tien = models.DecimalField(max_digits=12, decimal_places=0, default=0, editable=False, verbose_name="Thành tiền")
    

    class Meta:
        verbose_name = "Chi tiết đơn hàng"
        verbose_name_plural = "2b. Chi tiết đơn hàng"

    # Cập nhật hàng tồn
    def save(self, *args, **kwargs):
        validate_stock(self.so_luong, self.nhap_hang)  # Thêm kiểm tra xác thực

        self.thanh_tien = self.so_luong * self.don_gia
        # print("----------------------------da_ban trc:", self.nhap_hang.da_ban)
        # self.nhap_hang.da_ban += self.so_luong
        # print("----------------------------da_ban sau:", self.nhap_hang.da_ban)
        
        super().save(*args, **kwargs)

# Cập nhật hàng đã bán và tồn kho
@receiver(post_save, sender=DonHangChiTiet)
def update_nhaphang_on_donhangchitiet_save(sender, instance, created, **kwargs):   
    if created:
        nhap_hang = instance.nhap_hang
        nhap_hang.da_ban += instance.so_luong
        nhap_hang.ton_kho -= instance.so_luong
        if nhap_hang.ton_kho == 0:
            nhap_hang.tinh_trang = 'Hết hàng'
            nhap_hang.kich_hoat = False
        nhap_hang.save()




# class PhieuBaoGia(models.Model):
#     ngay_tao = models.DateTimeField()
#     han_hien = models.BooleanField()
#     chi_tiet = models.ForeignKey('phieu_bao_gia_chi_tiet.PhieuBaoGiaChiTiet', on_delete=models.CASCADE)
#     giao_dich = models.ForeignKey(GiaoDich, on_delete=models.CASCADE, null=True, blank=True)

# # Models for transaction details and quotation details would be defined in separate apps (e.g., giao_dich_chi_tiet, phieu_bao_gia_chi_tiet)


# Signal to update ton_kho on DonHangChiTiet save
# @receiver(pre_save, sender=DonHangChiTiet)
# def update_ton_kho(sender, instance, **kwargs):
#     # Validate stock before updating
#    validate_stock(instance.so_luong, instance.nhap_hang)

#     # Update ton_kho in NhapHang instance
#     nhap_hang = instance.nhap_hang
#     if nhap_hang:
#         nhap_hang.ton_kho = max(0, nhap_hang.ton_kho - instance.so_luong)

# # Ensure ton_kho is non-negative (optional)
# @receiver(pre_save, sender=NhapHang)
# def ensure_ton_kho_non_negative(sender, instance, **kwargs):
#     instance.ton_kho = max(0, instance.ton_kho)  # Set ton_kho to 0 if negative


@receiver(post_delete, sender=LoaiGiaoDich)
@receiver(post_delete, sender=DonHang)
@receiver(post_delete, sender=DonHangChiTiet)
@receiver(post_delete, sender=DonHangLoaiGiaoDich)

def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

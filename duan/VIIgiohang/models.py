from django.db import models

from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save

from Ithongtincongty.models import LopCoBan, ChiNhanh
# from IVdoitac.models import NhaCungCap, KhachHang
from IIIquanlykho.models import NhapHang

class GioHang(LopCoBan):
    ten_giao_dich = models.CharField(max_length=255, verbose_name='Tên giao dịch')
    class Meta:
        verbose_name = "Danh mục giao dịch"
        verbose_name_plural = "1. Danh mục giao dịch"

    def __str__(self):
        return self.ten_giao_dich



# class DonHang(LopCoBan):
#     trang_thai_don_hang_choices = (
#         ("cho_xu_ly", "Chờ xử lý"),
#         ("da_xac_nhan", "Đã xác nhận"),
#         ("dang_giao_hang", "Đang giao hàng"),
#         ("da_hoan_thanh", "Đã hoàn thành"),
#         ("da_huy", "Đã hủy"),
#     )
#     loai_giao_dich = models.ManyToManyField(LoaiGiaoDich, through='DonHangLoaiGiaoDich')

#     # loai_giao_dich = models.ForeignKey(LoaiGiaoDich, on_delete=models.CASCADE, default=1, verbose_name='Loại giao dịch')
#     ngay_tao = models.DateTimeField(auto_created=True, verbose_name='Ngày tạo', null=True, editable=False)
#     nhan_vien = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Nhân viên')
#     khach_hang = models.ForeignKey('IVdoitac.KhachHang', on_delete=models.CASCADE, verbose_name='Khách hàng')  # Assuming 'IVdoitac.KhachHang' for customer model
#     chi_nhanh = models.ForeignKey('Ithongtincongty.ChiNhanh', on_delete=models.CASCADE, default=1, verbose_name='Chi nhánh')  # Assuming 'Ithongtincongty.ChiNhanh' for branch model

#     # Consider using a ManyToManyField for selecting multiple products
#     # ten_san_pham = models.ForeignKey(NhapHang.ten_san_pham, on_delete=models.CASCADE)
#     san_pham = models.ManyToManyField(NhapHang, through='DonHangChiTiet', verbose_name='Sản phẩm')

#     trang_thai_don_hang = models.CharField(
#         max_length=20, choices=trang_thai_don_hang_choices, default="cho_xu_ly", verbose_name="Trạng thái đơn hàng"
#     )
#     tong_gia_tri = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="Tổng giá trị")
#     tam_ung = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='Số tiền tạm ứng')
#     so_tien_con_lai = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='Số tiền còn lại')


#     phuong_thuc_thanh_toan = models.CharField(max_length=50, verbose_name="Phương thức thanh toán", blank=True)
#     ghi_chu = models.TextField(blank=True, verbose_name="Ghi chú")

#     class Meta:
#         verbose_name = "Đơn hàng"
#         verbose_name_plural = "2. Đơn hàng"
    
#     def save(self, *args, **kwargs):
#         # Cập nhật `so_tien_con_lai` khi lưu đơn hàng
#         self.so_tien_con_lai = self.tong_gia_tri - self.tam_ung
#         super().save(*args, **kwargs)


#     def __str__(self):
#         return f"Đơn hàng {self.id} - {self.khach_hang}"
    


# @receiver(post_delete, sender=LoaiGiaoDich)


def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

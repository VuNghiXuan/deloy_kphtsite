from django.contrib import admin
from .models import LoaiGiaoDich, DonHang,DonHangLoaiGiaoDich, DonHangChiTiet

class LoaiGiaoDichAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu',
        'ten_giao_dich',
        
    )
    list_filter = ('ten_giao_dich',)
    search_fields = ('ten_giao_dich',)
    list_per_page = 20

class DonHangAdmin(admin.ModelAdmin):
    list_display = (
        'so_thu_tu',
        'ngay_tao',
        'nhan_vien',
        'khach_hang',
        'chi_nhanh',
        'trang_thai_don_hang',
        'tong_gia_tri',
        'tam_ung',
        'so_tien_con_lai',
        'phuong_thuc_thanh_toan',
        'get_khach_hang_ten',  # Custom method to display customer name
    )
    list_filter = ('trang_thai_don_hang', 'chi_nhanh', 'ngay_tao')
    search_fields = ('id', 'trang_thai_don_hang', 'khach_hang__ho_ten')  # Assuming 'ho_ten' field in 'KhachHang' model
    list_per_page = 20

    def get_khach_hang_ten(self, obj):
        return obj.khach_hang.ho_ten  # Assuming 'ho_ten' field exists
    get_khach_hang_ten.short_description = 'Tên khách hàng'

    # Consider adding custom methods for displaying other relevant data (e.g., order details)

class DonHangLoaiGiaoDichAdmin(admin.ModelAdmin):
    list_display = (
        'don_hang',
        'loai_giao_dich',
    )
    list_filter = ('don_hang',)
    search_fields = ('don_hang__id', 'loai_giao_dich__ten_giao_dich')
    list_per_page = 20

class DonHangChiTietAdmin(admin.ModelAdmin):
    list_display = (
        'don_hang',
        'nhap_hang',
        'so_luong',
        'don_gia',
        'thanh_tien',
    )
    list_filter = ('don_hang',)
    search_fields = ('don_hang__id', 'nhap_hang__ten_san_pham')  # Assuming 'ten_san_pham' field in 'NhapHang' model
    list_per_page = 20


admin.site.register(LoaiGiaoDich, LoaiGiaoDichAdmin)
admin.site.register(DonHang, DonHangAdmin)
admin.site.register(DonHangLoaiGiaoDich, DonHangLoaiGiaoDichAdmin)
admin.site.register(DonHangChiTiet, DonHangChiTietAdmin)

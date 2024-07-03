from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import (
    QuayLon,
    QuayNho,
    NhomVang,
    LoaiVang,
    NhomHang,
    NhapHang,
    #SanPham,
)

# **QuayLonAdmin** - Quản lý quầy lớn
class QuayLonAdmin(admin.ModelAdmin):
    list_display = ( 'so_thu_tu', 'ten_quay_lon', 'kich_hoat', 'chi_nhanh', 'kich_hoat',)  # Use 'ma_quay_lon' field if it exists#'ma_quay_lon',
    list_filter = ('ten_quay_lon',)  # 'ten_chi_nhanh' can be added for filtering by branch if desired
    search_fields = ( 'ten_quay_lon', )  # Search by 'ma_quay_lon' if it exists 'ma_quay_lon',

    def __str__(self):
        return self.ten_quay_lon


# **QuayNhoAdmin** - Quản lý quầy nhỏ
class QuayNhoAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu',  'ten_quay_nho', 'quay_lon', 'chi_nhanh', 'kich_hoat',)  # Use 'ma_quay_nho' field if it exists'ma_quay_nho',
    list_filter = ('ten_quay_nho', 'quay_lon', 'chi_nhanh')
    search_fields = ( 'ten_quay_nho', 'quay_lon__ten_quay_lon')  # Search by foreign key field

    def __str__(self):
        return self.ten_quay_nho


# **NhomVangAdmin** - Quản lý nhóm vàng
class NhomVangAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_nhom_vang',)
    search_fields = ('ten_nhom_vang',)

    def __str__(self):
        return self.ten_nhom_vang


# **LoaiVangAdmin** - Quản lý loại vàng
class LoaiVangAdmin(admin.ModelAdmin):
    list_display = (
        'so_thu_tu', 
        'ten_loai_vang',
        'nhom_vang',
        'tuoi_vang',
        'tuoi_pho',
        'don_vi_tinh',
        'lamtron_giamuaban',
        'hienbang_dientu',
        'kich_hoat',
    )
    list_filter = ('nhom_vang', 'don_vi_tinh', 'lamtron_giamuaban', 'kich_hoat')
    search_fields = (
        'ten_loai_vang',
        'nhom_vang__ten_nhom_vang',
        'tuoi_vang',
        'tuoi_pho',
        'don_vi_tinh',
    )

    def __str__(self):
        return self.ten_loai_vang


# **NhomHangAdmin** - Quản lý nhóm hàng
class NhomHangAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ma_nhom_hang', 'quay_nho', 'ten_nhom_hang','kich_hoat',)
    search_fields = ('ma_nhom_hang', 'ten_nhom_hang',)

    def __str__(self):
        return self.ten_nhom_hang


# **NhapHangAdmin** - Quản lý nhập hàng
class NhapHangAdmin(admin.ModelAdmin):
    list_display = (
          # Use 'ma_nhap_hang' field if it exists'ma_nhap_hang',
        'so_thu_tu',          
        'ten_san_pham', 
        'ma_san_pham',
        'so_luong',
        'da_ban',
        'ton_kho',
        'tl_vang_hot',
        'tl_hot',
        'tl_vang',
        'cong_von',
        'cong_ban',
        'tien_hot',
        'gia_ban_mon',
        'so_lo',
        'tinh_trang',
        'hinh_anh',
        'loai_vang', 
        'nhom_hang',
        'ten_chi_nhanh',
        'nhan_vien',        
        'quay_nho',
        'quay_lon',
        'nha_cung_cap',
        'ngay_nhap',
        'tem',
        'kich_hoat',
        # 'get_cong_ty',  # Custom method to display company name
    )
    list_filter = ('ten_chi_nhanh', 'quay_nho', 'quay_lon')
    search_fields = (
          # Use 'ma_nhap_hang' field if it exists 'ma_nhap_hang',
        'so_thu_tu', 
        'ten_nhan_vien',
        'quay_nho__ten_quay_nho',
        'quay_lon__ten_quay_lon',
        'ten_chi_nhanh__ten_chi_nhanh',
        'nha_cung_cap',
        'kich_hoat',
    )
    list_per_page = 20
    readonly_fields = ["image", 'barcode']
    def image(self, obj):
        if obj.hinh_anh:
            return mark_safe(f'<img src="{obj.hinh_anh.url}" alt="{obj.ten_san_pham}" style="max-width:100px;max-height:100px;" />')
        else:
            return "Không có ảnh"
    image.short_description = 'Ảnh sản phẩm'
    def barcode(self, obj):
        if obj.tem:
            print("---------------------------", obj.tem.url)
            return mark_safe(f'<img src="{obj.tem.url}" alt="{obj.ma_san_pham}" style="max-width:100px;max-height:100px;" />')
        else:
            return "Không có mã vạch"
    barcode.short_description = 'Ảnh mã vạch'
    

    # def get_cong_ty(self, obj):
    # # Assuming the NhapHang model has a foreign key to CongTy named 'cong_ty'
    #     if obj.cong_ty:
    #         return obj.cong_ty.ten_cong_ty
    #     else:
    #         return ''

# class SanPhamAdmin(admin.ModelAdmin):
#     # list_display = ('tem', 'ten_san_pham', 'loai_vang', 'nhom_hang', 'ten_chi_nhanh','kich_hoat',)  # Fields to display in the admin list
#     # list_filter = ('loai_vang', 'nhom_hang', 'ten_chi_nhanh')  # Fields to filter by in the admin list
#     # search_fields = ('tem', 'ten_san_pham')  # Fields to search by in the admin list
#     # readonly_fields = ('tem',)  # Fields that cannot be edited in the admin interface (optional)
#     pass


admin.site.register(QuayLon, QuayLonAdmin)
admin.site.register(QuayNho, QuayNhoAdmin)
admin.site.register(NhomVang, NhomVangAdmin)
admin.site.register(LoaiVang, LoaiVangAdmin)
admin.site.register(NhomHang, NhomHangAdmin)
admin.site.register(NhapHang, NhapHangAdmin)
# admin.site.register(SanPham, SanPhamAdmin)  # Register the SanPham model with the admin site        
# admin.site.register(SanPham, SanPhamAdmin)



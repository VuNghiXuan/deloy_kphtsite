from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import NhaCungCap, NhaVanChuyen, ThoNgoai, KhachHang

class NhaCungCapAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'nha_cung_cap',)  # Display only 'ten_nha_cung_cap' field
    search_fields = ('ten_nha_cung_cap',)  # Enable search by 'ten_nha_cung_cap'
    # Add more fields to list_display and search_fields as needed

class NhaVanChuyenAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'nha_van_chuyen',)  # Display only 'ten_nha_van_chuyen' field
    search_fields = ('ten_nha_van_chuyen',)  # Enable search by 'ten_nha_van_chuyen'
    # Add more fields to list_display and search_fields as needed

class ThoNgoaiAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_tho',)  # Display only 'ten_tho' field
    search_fields = ('ten_tho',)  # Enable search by 'ten_tho'
    # Add more fields to list_display and search_fields as needed

class KhachHangAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ho_ten','dia_chi','sdt', 'diem', 'so_cccd',"anh_dai_dien")  # Display only 'ten_tho' field
    search_fields = ('ho_ten', 'dia_chi','sdt','so_cccd')  # Enable search by 'ten_tho'
    list_filter =['ho_ten', 'dia_chi','sdt','so_cccd']
    
    # Add more fields to list_display and search_fields as needed
    readonly_fields = ["image"]

    def image(self, obj):
            if obj.anh_dai_dien:
                return mark_safe(f'<img src="{obj.anh_dai_dien.url}" alt="{obj.ho_ten}" style="max-wso_thu_tuth:100px;max-height:100px;" />')
            else:
                return "Không có ảnh"

    image.short_description = 'Ảnh'

# Register the models with their respective admins
admin.site.register(NhaCungCap, NhaCungCapAdmin)
admin.site.register(NhaVanChuyen, NhaVanChuyenAdmin)
admin.site.register(ThoNgoai, ThoNgoaiAdmin)
admin.site.register(KhachHang, KhachHangAdmin)

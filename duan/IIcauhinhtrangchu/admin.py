from django.contrib import admin
from .models import BoSuuTap
from django.utils.safestring import mark_safe

# Register your models here.

class BoSuuTapAdmin(admin.ModelAdmin):
    list_display = (
          # Use 'ma_nhap_hang' field if it exists'ma_nhap_hang',
        'so_thu_tu',          
        'ten_bo_suu_tap',         
        'kich_hoat',
        # 'get_cong_ty',  # Custom method to display company name
    )
    list_filter = ('ten_bo_suu_tap', )
    search_fields = (
          # Use 'ma_nhap_hang' field if it exists 'ma_nhap_hang',
        'ten_bo_suu_tap',         
    )
    list_per_page = 20
    readonly_fields = ["image",]
    def image(self, obj):
        if obj.anh_dai_dien:
            return mark_safe(f'<img src="{obj.anh_dai_dien.url}" alt="{obj.ten_bo_suu_tap}" style="max-width:100px;max-height:100px;" />')
        else:
            return "Không có ảnh"

admin.site.register(BoSuuTap, BoSuuTapAdmin)
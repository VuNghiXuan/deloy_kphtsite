from django.contrib import admin
from .models import GiaVang
# Register your models here.
class GiaVangAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'loai_vang', 'gia_mua', 'gia_ban',)  # Fields to display in the admin list
    # list_filter = ('loai_vang', 'nhom_hang', 'ten_chi_nhanh')  # Fields to filter by in the admin list
    # search_fields = ('tem', 'ten_san_pham')  # Fields to search by in the admin list
    # readonly_fields = ('tem',)  # Fields that cannot be edited in the admin interface (optional)

    

admin.site.register(GiaVang, GiaVangAdmin)
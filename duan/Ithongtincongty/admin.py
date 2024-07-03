
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from .models import CongTy, ChiNhanh, PhongBan, NhanVien, NhiemVu
from django.utils.safestring import mark_safe

# admin.site.register(CongTy)
# admin.site.register(ChiNhanh)
# admin.site.register(PhongBan)
# admin.site.register(NhanVien)
# admin.site.register(NhiemVu)
# admin.site.register(User)
# admin.site.register(Permission)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


@admin.register(CongTy)
class CongTyAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_cong_ty', 'ten_viet_tat', 'dia_chi', 'hotline', "kick_hoat_web")
    list_filter =['ten_cong_ty', 'ten_viet_tat', "kick_hoat_web"]
    search_fields = ('ten_cong_ty', 'ten_viet_tat')
    readonly_fields = ["image"]

    def image(self, obj):
        if obj.logoCongTy:
            return mark_safe(f'<img src="{obj.logoCongTy.url}" alt="{obj.ten_cong_ty}" style="max-wso_thu_tuth:100px;max-height:100px;" />')
        else:
            return "Không có ảnh"

    image.short_description = 'Logo công ty'
    # admin.site.register(CongTy)

    # def image(self, obj):
    #     return mark_safe(
    #          f'<img src="congty/%Y/%m{obj.image.url}" alt="{obj.ten_cong_ty}"/>'
    #         # '''
    #         #     <img src= /media/{img_url} alt = '{alt}'/>
    #         # '''.format(img_url=obj.image.name, alt= obj.ten_cong_ty)        
    #         )

@admin.register(ChiNhanh)
class ChiNhanhAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_chi_nhanh', 'ten_viet_tat', 'dia_chi', 'hotline', 'cong_ty', 'kich_hoat',)
    search_fields = ('ten_chi_nhanh', 'ten_viet_tat')


@admin.register(PhongBan)
class PhongBanAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_phong_ban','kich_hoat',)  # Bỏ chú thích
    search_fields = ('ten_phong_ban',)  # Bỏ chú thích


@admin.register(NhiemVu)
class NhiemVuAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_nhiem_vu','kich_hoat',)
    search_fields = ('ten_nhiem_vu',)


@admin.register(NhanVien)
class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'ten_nhan_vien','chi_nhanh', 'kich_hoat',)  # Bỏ chú thích: 'anh_dai_dien','nhiem_vu'
    search_fields = ('ten_nhan_vien', 'chi_nhanh__ten_chi_nhanh')  # Bỏ chú thích
    autocomplete_fields = ['chi_nhanh']  # Bỏ chú thích
    filter_horizontal = ('nhiem_vu',)
    list_per_page = 20

# admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ( 'so_thu_tu', 'anh_dai_dien', )#'phong_ban','ten_nhan_vien','nhiem_vu''chi_nhanh',
    # search_fields = ('ten_nhan_vien', 'chi_nhanh__ten_chi_nhanh')#'phong_ban__ten_phong_ban',
    # autocomplete_fields = [ 'chi_nhanh']#'phong_ban','ten_nhan_vien',
    # filter_horizontal = ('nhiem_vu',)
    # list_per_page = 20
    


    # def get_username(self, obj):
    #     # Lấy username từ đối tượng NhanVien
    #     return obj.username

    # def set_username(self, request, queryset):
    #     # Cập nhật username cho các đối tượng NhanVien được chọn
    #     for obj in queryset:
    #         obj.username = request.POST['new_username']
    #         obj.save()

    # get_username.short_description = 'Tên đăng nhập'
    # set_username.short_description = 'Cập nhật tên đăng nhập'

    # list_display = ('so_thu_tu', 'username','anh_dai_dien', )  # Hiển thị username, 'chi_nhanh',
    # readonly_fields = ('username',)  # Cho phép người dùng chỉ đọc username
    # actions = [set_username]  # Thêm hành động cập nhật username
# admin.site.register(NhanVien, NhanVienAdmin)

# admin.site.register(Permission)

# Thay đổi vị trí thứ tự các app
# admin.site.set_app_ordering = ('app1', 'app2', 'app3')
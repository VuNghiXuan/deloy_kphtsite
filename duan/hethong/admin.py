from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import UserProfile


admin.site.register(UserProfile)

# mix profile infor and user: thêm phân quyền từ hệ thống
class ProfileInline(admin.StackedInline):
    model = UserProfile

# **UserProfileAdmin** 
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username',  'fist_name','last_name', 'email']
    inlines = [ProfileInline]
    
    list_per_page = 20
    
# Unregister the old way
admin.site.unregister(User)

# Re - Register the new way
admin.site.register(User, UserAdmin)




# # **UserProfileAdmin** 
# class UserProfileAdmin(admin.ModelAdmin):
    
#     list_display = (
#           # Use 'ma_nhap_hang' field if it exists'ma_nhap_hang',
#         'so_thu_tu',          
#         'user', 
#         'phone',
#         'address',
#         'bank_account',
#         'id_card',
#         'avatar',
        
#         'kich_hoat',
#         # 'get_cong_ty',  # Custom method to display company name
#     )
#     # list_filter = ['username', 'fist_name', 'last_name','email']
#     # search_fields = ( 'username', 'fist_name', 'last_name','email')
#     list_per_page = 20
#     readonly_fields = ["image"]
#     def image(self, obj):
#         if obj.avatar:
#             return mark_safe(f'<img src="{obj.avatar.url}" alt="{obj.user}" style="max-width:100px;max-height:100px;" />')
#         else:
#             return "Không có ảnh"
#     image.short_description = 'Ảnh đại diện'

# admin.site.register(UserProfile, UserProfileAdmin)






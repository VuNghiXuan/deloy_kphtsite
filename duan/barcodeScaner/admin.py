from django.contrib import admin
from .models import Barcode

# Register your models here.
class BarcodeAdmin(admin.ModelAdmin):
    list_display = ('so_thu_tu', 'du_lieu', 'ngay_tao', 'kich_hoat',)  # Fields to display in the admin list
    list_filter = ('du_lieu', 'ngay_tao', )  # Fields to filter by in the admin list
    search_fields = ('du_lieu', 'ngay_tao', )  # Fields to search by in the admin list
    # readonly_fields = ('tem',)  # Fields that cannot be edited in the admin interface (optional)
#     pass


admin.site.register(Barcode, BarcodeAdmin)
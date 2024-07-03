from django.contrib import admin
from .models import ShippingAddress, Order, ItemOrder
from django.contrib.auth.models import User

# Đăng ký model tại đây.
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(ItemOrder)

# Tạo OrderItem Inline (Tùy chọn)
class OrderItemInline(admin.StackedInline):
    model = ItemOrder
    extra = 0
    # min_num_inlines = 0  # Tùy chọn, kiểm soát số lượng tối thiểu biểu mẫu được hiển thị

# Mở rộng Quản trị viên Đơn hàng (Tùy chọn)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ['date_order']
    fields = ['user', 'full_name', 'shipping_address', 'email', 'amount_paid', 'date_order', 'shipped', 'date_shipped']
    inlines = [OrderItemInline] #if OrderItemInline else []  # Bao gồm inline chỉ khi được định nghĩa

# Hủy đăng ký và Đăng ký lại để Cập nhật Tùy chọn (nếu cần)
admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)

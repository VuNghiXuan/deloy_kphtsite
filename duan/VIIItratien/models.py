from django.db import models
from django.contrib.auth.models import User
from IIIquanlykho.models import NhapHang
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime

# Create your models here.

class ShippingAddress(models.Model):
    #null=True: Dành cho khách hàng chưa đăng ký.
    # blank=True: Điền tên sau
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Mã khách hàng') 
    shipping_full_name = models.CharField(max_length=255, verbose_name="Họ và tên")
    shipping_address = models.CharField(max_length=255, verbose_name="Địa chỉ nhận hàng")

    shipping_phone = models.CharField(max_length=20, blank= True, verbose_name= 'Số điện thoại')
    # shipping_bank_account = models.CharField(max_length=20, null=True, blank= True, verbose_name= 'Tài khoản ngân hàng')
    shipping_id_card = models.CharField(max_length=20, blank= True, null=True, verbose_name= 'Căn cước công dân')

    # shipping_email = models.CharField(max_length=255, verbose_name="Email", blank=True)
    # shipping_address = models.CharField(max_length=255, verbose_name="Địa chỉ")

    # Don't pluralize address
    class Meta:
        verbose_name_plural = "Địa chỉ giao hàng"

    def __str__(self):
        return f'Địa chỉ giao hàng -{str(self.id)}'


# Create Shipping User
def create_shipping(sender, instance, created,  **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

# Automate the shipping things
post_save.connect(create_shipping, sender=User)


# Create Order models
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Khách hàng') 
    full_name = models.CharField(max_length=255, verbose_name="Người nhận")
    email = models.CharField(max_length=255, verbose_name="Email", blank=True)
    shipping_address = models.TextField(max_length=1500, verbose_name="Thông tin nhận hàng")
    
    # shipping_phone = models.CharField(max_length=20, blank= True, null= True, verbose_name= 'Số điện thoại')
    # shipping_bank_account = models.CharField(max_length=20, null=True, blank= True, verbose_name= 'Tài khoản ngân hàng')
    # shipping_id_card = models.CharField(max_length=20, blank= True, null=True, verbose_name= 'Căn cước công dân')

    amount_paid = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="Số tiền phải trả") 
    date_order = models.DateTimeField(auto_now_add=True, verbose_name="Ngày lập đơn hàng")
    shipped = models.BooleanField(default=False, verbose_name="Khách đã nhận hàng")
    date_shipped = models.DateTimeField(blank=True, null=True, verbose_name="Ngày nhận hàng")# Sử dụng pre_save để lưu ngày

    # Don't pluralize address
    class Meta:
        verbose_name_plural = "Đơn hàng"

    def __str__(self):
        return f'Đơn hàng -{str(self.id)}'

# Auto save datetime when goods to customer (using objects.get method)
@receiver(pre_save, sender=Order)
def set_datetime_for_shipped(sender, instance, **kwargs):
    if instance.pk:
        now = datetime.datetime.now()
        try:
            # Attempt to retrieve existing Order object
            existing_order = Order.objects.get(pk=instance.pk)
        except Order.DoesNotExist:
            # Handle case where Order might not exist yet (e.g., initial creation)
            pass
        else:
            if instance.shipped and not existing_order.shipped:
                instance.date_shipped = now




# Create Order Items models
class ItemOrder(models.Model):
    # foreignKey
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, verbose_name='Đơn hàng') 
    product = models.ForeignKey(NhapHang, on_delete=models.CASCADE, null=True,  verbose_name='Sản phẩm') 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Khách hàng') 
    quantity = models.PositiveBigIntegerField(default=1, verbose_name='Số lượng')
    price = models.DecimalField( decimal_places=0, max_digits=12, verbose_name="Giá (đồng)") 

    # Don't pluralize address
    class Meta:
        verbose_name_plural = "Đơn hàng theo món"

    def __str__(self):
        return f'Đơn hàng theo món -{str(self.id)}'
    
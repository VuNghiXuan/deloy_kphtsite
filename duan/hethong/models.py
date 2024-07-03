from django.db import models

# Create your models here.
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from Ithongtincongty.models import LopCoBan

# Create profile User
class UserProfile(LopCoBan):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name='Tên đăng nhập')
    date_modified = models.DateTimeField(User, auto_now=True)#, verbose_name='Ngày tạo'
    address = models.CharField(max_length=200, blank= True, verbose_name= 'Địa chỉ')
    phone = models.CharField(max_length=20, blank= True, verbose_name= 'Số điện thoại')
    id_card = models.CharField(max_length=20, blank= True, verbose_name= 'Căn cước công dân')
    bank_account = models.CharField(max_length=20, blank= True, verbose_name= 'Tài khoản ngân hàng')
    avatar = models.ImageField(upload_to="users/%Y/%m", verbose_name="Ảnh đại diện", null=True, blank=True)
    old_cart = models.CharField(max_length=200, blank= True, verbose_name= 'Giỏ hàng cũ', null=True)
    # city = models.CharField(max_length=200, blank= True, verbose_name= 'Thành phố')
    # province = models.CharField(max_length=200, blank= True, verbose_name= 'Tỉnh')

    class Meta:
        verbose_name = "Thông tin tài khoản"
        verbose_name_plural = "1. Thông tin tài khoản"
        

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created,  **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

# Automate the profile things
post_save.connect(create_user_profile, sender=User)

# Lưu số thứ tự
@receiver(post_delete, sender=UserProfile)
def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 
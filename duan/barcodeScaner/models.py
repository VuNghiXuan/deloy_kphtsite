from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from Ithongtincongty.models import LopCoBan

# Create your models here.
class Barcode(LopCoBan):
    du_lieu = models.CharField(max_length=255, verbose_name= "Dữ liệu barcode")
    ngay_tao = models.DateTimeField(auto_now_add=True, verbose_name= "Ngày tạo")

    def __str__(self) -> str:
        return f'{self.du_lieu} - {self.ngay_tao}'
    

@receiver(post_delete, sender=Barcode)
def update_so_thu_tu(sender, instance, **kwargs):
    stts = sender.objects.all()
    count = 1
    for stt in stts:
        stt.so_thu_tu = count
        count += 1
        stt.save() 

        